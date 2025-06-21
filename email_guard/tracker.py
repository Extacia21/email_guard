import os
import sqlite3
import datetime
from flask import Flask, request, send_file, g, render_template_string

DATABASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'email_opens.db')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS email_opens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email_id TEXT NOT NULL,
                opened_at TEXT NOT NULL
            )
        ''')
        conn.commit()

def create_app():
    app = Flask(__name__)
    init_db()

    @app.teardown_appcontext
    def close_connection(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

    @app.route("/")
    def index():
        db = get_db()
        cursor = db.execute('SELECT email_id, opened_at FROM email_opens ORDER BY opened_at DESC LIMIT 50')
        rows = cursor.fetchall()
        html = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1" />
          <title>Email Opens Dashboard</title>
          <style>
            body {
              font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
              background: #f4f6f8;
              color: #333;
              margin: 20px auto;
              max-width: 900px;
              padding: 0 15px;
            }
            h2 {
              text-align: center;
              color: #004080;
              margin-bottom: 25px;
            }
            table {
              width: 100%;
              border-collapse: collapse;
              box-shadow: 0 2px 5px rgba(0,0,0,0.1);
              background: white;
              border-radius: 8px;
              overflow: hidden;
            }
            th, td {
              padding: 12px 15px;
              text-align: left;
            }
            th {
              background-color: #004080;
              color: white;
              font-weight: 600;
              font-size: 1rem;
            }
            tr:nth-child(even) {
              background-color: #f9fbfd;
            }
            tr:hover {
              background-color: #e1f0ff;
              cursor: default;
            }
            footer {
              margin-top: 30px;
              text-align: center;
              font-size: 0.9rem;
              color: #777;
            }
          </style>
        </head>
        <body>
          <h2>Email Opens (Latest 50)</h2>
          <table>
            <thead>
              <tr><th>Email ID</th><th>Opened At (UTC)</th></tr>
            </thead>
            <tbody>
              {% for email_id, opened_at in rows %}
              <tr>
                <td>{{ email_id }}</td>
                <td>{{ opened_at }}</td>
              </tr>
              {% endfor %}
            </tbody>
          </table>
          <footer>Powered by Email Guard &mdash; Your Email Security Tracker</footer>
        </body>
        </html>
        '''
        return render_template_string(html, rows=rows)

    @app.route("/track_open")
    def track_open():
        email_id = request.args.get("email_id")
        if email_id:
            db = get_db()
            db.execute(
                'INSERT INTO email_opens (email_id, opened_at) VALUES (?, ?)',
                (email_id, datetime.datetime.utcnow().isoformat())
            )
            db.commit()
            print(f"Email opened: {email_id}")
        pixel_path = os.path.join(app.root_path, '..', 'pixel.png')
        return send_file(pixel_path, mimetype="image/png")

    return app
