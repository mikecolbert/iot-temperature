
from flask import Flask
from flask import request
import os

app = Flask(__name__)

dbuser = os.environ.get('DBUSER')
dbpass = os.environ.get('DBPASS')
dbhost = os.environ.get('DBHOST')
dbname = os.environ.get('DBNAME')

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

@app.route('/')
def index():
    return "Temperature API" 


@app.route('/temperature-data/sensors')
def sensors():
    return dbname


if __name__ == '__main__':
    app.run(debug=True)
