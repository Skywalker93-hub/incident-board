from flask import Flask 

app = Flask(__name__)

#Create a variable that describe an one of test incindent
incidents=[{"id": 1, "title": "Сайт недоступен"}]

@app.get("/incidents")
def get_incidents():
    return incidents

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


