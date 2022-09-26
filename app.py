
from flask import Flask
from flask import request
#from dotenv import load_dotenv
import os

#load_dotenv()

app = Flask(__name__)

#dbuser = os.getenv('DBUSER')
#dbpass = os.getenv('DBPASS')
dbhost = os.getenv('DBHOST')
#dbname = os.getenv('DBNAME')

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

#print(dbuser)

@app.route('/')
def index():
    return "Temperature API" 


@app.route('/temperature-data/sensors')
def sensors():
    return dbhost


if __name__ == '__main__':
    app.run(debug=True)
