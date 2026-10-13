
# Incident Board

A web application for tracking incidents and their resolution status.
Users can report incidents, view the incident list, and mark incidents as resolved.

## Components

There are three parts:

**Frontend**: Nginx serves the web page, and its JavaScript sends API requests. Nginx forwards GET, POST, and PATCH requests to the backend.

**Backend**: A Python script using Flask handles requests to list, create, and resolve incidents.

**Database**: PostgreSQL stores incidents and their statuses. The backend reads and writes this data.

## Architecture

```
User
  |
  v
Frontend (Nginx + HTML/JavaScript)
  |
  | HTTP API
  v
Backend (Python + Flask)
  |
  | SQL
  v
Database (PostgreSQL)
```
