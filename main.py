import sqlite3
from flask import Flask, render_template, request, g

app = Flask(__name__)

# load the configuration to smooth database connections
app.config.from_object(__name__)

# database details - to remove some duplication
db_name = 'population_data.db'

# code based on example at https://github.com/mjhea0/flaskr-tdd

def connect_db():
    conn = sqlite3.connect(
        db_name, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn.row_factory = sqlite3.Row
    return conn


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route("/")
def main():
    db = get_db()
    cur = db.execute("select * from countries_population")
    rows = cur.fetchall()
    return render_template("index.html", rows=rows)
