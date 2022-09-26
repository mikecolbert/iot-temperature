import mysql.connector
from mysql.connector import Error
from flask import Flask
from flask import request
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

dbuser = os.environ.get('DBUSER')
dbpass = os.environ.get('DBPASS')
dbhost = os.environ.get('DBHOST')
dbname = os.environ.get('DBNAME')

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


@app.route('/', methods=['GET'])
def index():
    return "Temperature API"

@app.route('/temperature-data/', methods=['GET', 'POST'])
def temperatures():
    if request.method == 'GET':
        conn = mysql.connector.connect(host=dbhost, database=dbname, user=dbuser, password=dbpass)
        cur = conn.cursor()

        sql = "SELECT * FROM temperatureLog ORDER BY readTime DESC"
        cur.execute(sql)
        print(sql)
        results = cur.fetchall()

        print("----------")
        print("Total number of rows in table: ", cur.rowcount)
        print("----------")
        print(results)
        
        cur.close()
        conn.close()
            
        return (results)

    if request.method == 'POST':
        form = request.form
        sensorId = form['sensor']
        temperature = form['temp']
        humidity = form['humidity']
        
        conn = mysql.connector.connect(host=dbhost, database=dbname, user=dbuser, password=dbpass)
        cur = conn.cursor()

        sql = "INSERT INTO temperatures(readTime, sensorId, temperature, humidity) VALUES(NOW(), %s, %s, %s)",(sensorId, temperature, humidity)
        cur.execute(sql)
        print(sql)
        results = cur.fetchall()

        print("----------")
        print("Total number of rows in table: ", cur.rowcount)
        print("----------")
        print(results)
        
        cur.close()
        conn.close()
            
        return (results)


@app.route('/temperature-data/sensors')
def sensors():
    return "Sensors"



if __name__ == '__main__':
    app.run(debug=True)
