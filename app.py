import sqlite3
from flask import Flask, render_template, request, g

app = Flask(__name__)

# load the configuration to smooth database connections
app.config.from_object(__name__)

# database details - to remove some duplication
db_name = 'population_data.db'

# code based on example at https://github.com/scharlau/shopping_testing_p/blob/main/shopping.py

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
  
# ----------

# list of years that can be assessed
all_years = [2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000]

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search_country")
def search_country():
  db = get_db()
  cur = db.execute("SELECT id,country FROM countries")
  all_countries = cur.fetchall()
  return render_template("search_country.html", countries=all_countries)


@app.route("/search_year", methods = ["GET", "POST"])
def search_year():
  db = get_db()
  year = 2018
  if request.method == "POST":
    year = request.form["year"]
  
  cur = db.execute(""" SELECT *
                        FROM clean_fuel_total_population
                        INNER JOIN countries 
                        ON clean_fuel_total_population.country_id = countries.id
                        INNER JOIN clean_fuel_rural_population
                        ON clean_fuel_rural_population.id = clean_fuel_total_population.id
                        INNER JOIN clean_fuel_urban_population
                        ON clean_fuel_urban_population.id = clean_fuel_total_population.id
                        WHERE clean_fuel_total_population.year_eval=?
    """, (year,))
  rows = cur.fetchall()
  return render_template("search_year.html", rows=rows, all_years=all_years, year=year)


@app.route("/country_detail/<id>")
def country_detail(id):
  db = get_db()
  cur = db.execute(""" SELECT *
                        FROM clean_fuel_total_population
                        INNER JOIN countries 
                        ON clean_fuel_total_population.country_id = countries.id
                        INNER JOIN clean_fuel_rural_population
                        ON clean_fuel_rural_population.id = clean_fuel_total_population.id
                        INNER JOIN clean_fuel_urban_population
                        ON clean_fuel_urban_population.id = clean_fuel_total_population.id
                        WHERE countries.id = ?
  """, (id,))
  rows = cur.fetchall()
  return render_template("country_detail.html", id=id, rows=rows)


@app.route("/compare", methods = ["GET", "POST"])
def compare():
  db = get_db()
  country_1 = ''
  country_2 = ''
  year_1 = ''
  year_2 = ''
  country_1_details = []
  country_2_details  = []

  cur = db.execute("SELECT id,country FROM countries")
  all_countries = cur.fetchall()

  if request.method == "POST":
    country_1 = request.form["country1"]
    country_2 = request.form["country2"]
    year_1 = request.form["year1"]
    year_2 = request.form["year2"]
    print(country_1, country_2, year_1, year_2)
  
    cur = db.execute(""" SELECT *
                          FROM clean_fuel_total_population
                          INNER JOIN countries 
                          ON clean_fuel_total_population.country_id = countries.id
                          INNER JOIN clean_fuel_rural_population
                          ON clean_fuel_rural_population.id = clean_fuel_total_population.id
                          INNER JOIN clean_fuel_urban_population
                          ON clean_fuel_urban_population.id = clean_fuel_total_population.id
                          WHERE countries.country = ? AND clean_fuel_total_population.year_eval=?
    """, (country_1, year_1,))
    country_1_details = cur.fetchall()
    
    cur = db.execute(""" SELECT *
                          FROM clean_fuel_total_population
                          INNER JOIN countries 
                          ON clean_fuel_total_population.country_id = countries.id
                          INNER JOIN clean_fuel_rural_population
                          ON clean_fuel_rural_population.id = clean_fuel_total_population.id
                          INNER JOIN clean_fuel_urban_population
                          ON clean_fuel_urban_population.id = clean_fuel_total_population.id
                          WHERE countries.country = ? AND clean_fuel_total_population.year_eval=?
    """, (country_2, year_2,))
    country_2_details = cur.fetchall()

  return render_template("compare.html", country1_details = country_1_details, country2_details = country_2_details, all_countries=all_countries,
                          all_years=all_years, country_1 = country_1, country_2 = country_2, year_1=year_1, year_2=year_2)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404