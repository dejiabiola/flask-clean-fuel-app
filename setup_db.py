import csv
import sqlite3
from datetime import datetime

# open connection to the database
conn = sqlite3.connect('population_data.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
cur = conn.cursor()

#drop the tables
conn.execute("DROP TABLE IF EXISTS clean_fuel_total_population")
conn.execute("DROP TABLE IF EXISTS clean_fuel_rural_population")
conn.execute("DROP TABLE IF EXISTS clean_fuel_urban_population")
conn.execute("DROP TABLE IF EXISTS countries")
print("All tables dropped successfully")

# create the table
conn.execute("CREATE TABLE countries (id INTEGER PRIMARY KEY AUTOINCREMENT, country TEXT, created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL)")
conn.execute("CREATE TABLE clean_fuel_urban_population (id INTEGER PRIMARY KEY AUTOINCREMENT, country_id INTEGER, year_eval INTEGER, area TEXT, pop_number REAL, created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL, FOREIGN KEY(country_id) REFERENCES countries(id))")
conn.execute("CREATE TABLE clean_fuel_rural_population (id INTEGER PRIMARY KEY AUTOINCREMENT, country_id INTEGER, year_eval INTEGER, area TEXT, pop_number REAL, created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL, FOREIGN KEY(country_id) REFERENCES countries(id))")
conn.execute("CREATE TABLE clean_fuel_total_population (id INTEGER PRIMARY KEY AUTOINCREMENT, country_id INTEGER, year_eval INTEGER, area TEXT, pop_number REAL, created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL, FOREIGN KEY(country_id) REFERENCES countries(id))")
print("All new tables created successfully")


with open("./csv_files/Population_with_primary_reliance_on_clean_fuels_and_technologies_for_cooking_(in_millions).csv", newline='') as f:
  reader = csv.reader(f, delimiter=",")

  # skip the first line
  next(reader)
  country = ""
  for row in reader:
    if row[0] == country:
      next(reader)
    else:
      country = row[0]
      cur.execute("INSERT INTO countries VALUES(NULL,?,?)", (country, datetime.now()))
      conn.commit()

with open("./csv_files/Population_with_primary_reliance_on_clean_fuels_and_technologies_for_cooking_(in_millions).csv", newline='') as f:
  reader = csv.reader(f, delimiter=",")

  # skip the first line
  next(reader)
  cur.execute("SELECT * FROM countries")
  all_countries = cur.fetchall()
  for row in reader:
    area = row[3]
    year_eval = row[2]
    pop_number = float(row[6]) * 1000000
    for country in all_countries:
      country_id = country[0]
      if row[0] == country[1] and area == "Urban":
        print(country_id, country, year_eval, area, pop_number)
        cur.execute("INSERT INTO clean_fuel_urban_population VALUES(NULL,?,?,?,?,?)", (country_id, year_eval, area, pop_number, datetime.now()))
        conn.commit()
      elif row[0] == country[1] and area == "Rural":
        cur.execute("INSERT INTO clean_fuel_rural_population VALUES(NULL,?,?,?,?,?)", (country_id, year_eval, area, pop_number, datetime.now()))
        conn.commit()
      elif row[0] == country[1] and area == "Total":
        cur.execute("INSERT INTO clean_fuel_total_population VALUES(NULL,?,?,?,?,?)", (country_id, year_eval, area, pop_number, datetime.now()))
        conn.commit()
        
conn.close()


    



