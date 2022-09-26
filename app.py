
from flask import Flask
from flask import request
import pymysql
import os

app = Flask(__name__)

dbuser = os.environ.get('DBUSER')
dbpass = os.environ.get('DBPASS')
dbhost = os.environ.get('DBHOST')
dbname = os.environ.get('DBNAME')

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

conn = pymysql.connect(
        host = dbhost, 
        user = dbuser, 
        password = dbpass, 
        db = dbname, 
        ssl={'ca': './BaltimoreCyberTrustRoot.crt.pem'},
        cursorclass = pymysql.cursors.DictCursor)



@app.route('/')
def index():
    return "Temperature API" 

@app.route('/temperatures', methods=['GET', 'POST'])
def temperatures():
    #POST request
    if request.method == 'POST':
        form = request.form
        sensorId = form['sensor']
        temperature = form['temp']
        humidity = form['humidity']
        
        conn = pymysql.connect(
                host = dbhost, 
                user = dbuser, 
                password = dbpass, 
                db = dbname, 
                ssl={'ca': './BaltimoreCyberTrustRoot.crt.pem'},
                cursorclass = pymysql.cursors.DictCursor)
                
        cur = conn.cursor()
     
        query = "INSERT INTO temperaturelog(readTime, sensorId, temperature, humidity) VALUES(NOW(), %s, %s, %s)"
        cur.execute(query, sensorId, temperature, humidity)
        
        print("Record inserted into temperatures table.")
        
        cur.close()
        conn.close()
            
        return "insert complete"
    
    # GET request
    conn = pymysql.connect(
                host = dbhost, 
                user = dbuser, 
                password = dbpass, 
                db = dbname, 
                ssl={'ca': './BaltimoreCyberTrustRoot.crt.pem'},
                cursorclass = pymysql.cursors.DictCursor)

    cur = conn.cursor()

    query = "SELECT * FROM temperaturelog ORDER BY readTime DESC"
    cur.execute(query)
    
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
    return dbname


if __name__ == '__main__':
    app.run(debug=True)
