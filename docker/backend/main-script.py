import os

import psycopg
from psycopg.rows import dict_row
from flask import Flask, request

app = Flask(__name__)
app.json.ensure_ascii = False

@app.route('/health')
def health():
    return 'OK', 200

def connect_db():
    return psycopg.connect(
        host=os.environ["DB_HOST"],
        port=os.environ["DB_PORT"],
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        row_factory=dict_row,
    )


@app.get("/incidents")
def get_incidents():
    with connect_db() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT id, title, resolved FROM incidents ORDER BY id"
            )
            return cursor.fetchall()


@app.post("/incidents")
def create_incident():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return {"error": "Ожидается JSON-объект"}, 400

    title = data.get("title")

    if not isinstance(title, str) or not title.strip():
        return {"error": "Название обязательно"}, 400

    with connect_db() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO incidents (title)
                VALUES (%s)
                RETURNING id, title, resolved
                """,
                (title.strip(),),
            )
            incident = cursor.fetchone()

    return incident, 201


@app.patch("/incidents/<int:incident_id>")
def resolve_incident(incident_id):
    with connect_db() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE incidents
                SET resolved = TRUE
                WHERE id = %s
                RETURNING id, title, resolved
                """,
                (incident_id,),
            )
            incident = cursor.fetchone()

    if incident is None:
        return {"error": "Инцидент не найден"}, 404

    return incident


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
