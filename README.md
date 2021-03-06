# advanced-programming-assessment - Flask Web Application Built on Open Data

This is a flask application that built to display and compare data gotten freely from the internet. The data used in this application was gotten from the World Health Organisation. It is a statistical data on the population of each country in the 
world with primary reliance on clean fuels and technologies for cooking from the year 2000 to 2018. Further details on the data
can be found on the WHO website [here](https://www.who.int/data/gho/data/indicators/indicator-details/GHO/gho-phe-population-with-primary-reliance-on-clean-fuels-and-technologies-in-millions)

---
## Installation/Getting Started

Clone this git repository into your computer so that you have the documents to get started then open it in your preferred code editor.
Open your terminal and make sure the current location is in the directory you have cloned into your computer. Then run the following code to set up your virtual environment.

```
pyenv local 3.7.9 # this sets the local version of python to 3.7.9
python3 -m venv .venv # this creates the virtual environment
source .venv/bin/activate # this activates the virtual environment
```

After that runs successfully, the next step is to install all the libraries you would require to run the application successfully.
These libraries are already provided for in the requirements.txt file. Run the following lines in your terminal to get everything
installed

```
pip install --upgrade pip  # optional, this installs pip, and upgrades it if required.
pip install -r requirements.txt
```

## Setting up the database

The database used for this applications is a SQlite based application. SQlite is a small, full featured relational database
that comes bundled with python. 

All the code pertaining to creating the databse, parsing the csv file and inserting the data into the database can be found in the
`setup_db.py` file. The csv file itself is location inside the `csv_files` directory.

To set up the database, simply run the following command in your terminal
```
python3 setup_db.py
```
You will see a success prompt in the terminal when all files have been inserted successfully.


## Running the applications

There are couple of steps to take to run the application. Run the following commands in your terminal
```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
If you are using codio, you will need to use 
```
python3 -m flask run --host 0.0.0.0
```
instead of `flask run`

Once this is done, navigate to `localhost:5000` to view the webpage and access all the urls.


## Testing

The application uses Behave and Selenium to run behaviour driven test. This ensures that the program is running in a predictable manner. You can run the available tests by typing the following
command in your terminal.
```
behave
```

## Deployment

This application was deployed to Heroku using Gunicorn as it's HTTP server. Click the link below to check out the deployed website
https://pure-shelf-47022.herokuapp.com/









