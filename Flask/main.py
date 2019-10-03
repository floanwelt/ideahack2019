import json
import uuid
import time
from flask import request, jsonify
from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'corny'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Chorny'
app.config['MYSQL_DATABASE_DB'] = 'cornyChorny'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()



@app.route("/hotspots")
def hotspots():
    query = """SELECT lat, lon, radius, intensity FROM hotspots"""
    cursor.execute(query)
    result = cursor.fetchall()
    return json.dumps(result)

@app.route("/crimecenters")
def crimecenters():
    query = """SELECT lat, lon, radius FROM crimecenters"""
    cursor.execute(query)
    result = cursor.fetchall()
    return json.dumps(result)

@app.route("/incidents")
def incidents():
    query = """SELECT lat, lon, radius, intensity FROM incidents"""
    cursor.execute(query)
    result = cursor.fetchall()
    return json.dumps(result)

@app.route("/newIncident", methods=['POST'])
def newIncident():
    data = request.json
    json = jsonify(data)
    _id = str(uuid.uuid4())
    lat = json.lat
    lon = json.lon
    radius = 50
    intensity = 10
    timestamp = time.time()
    query = """INSERT INTO incidents(id, lat, lon, radius, intensity, timestamp) VALUES (%s, %s, %s, %s, %s, %s)""", \
            (_id, lat, lon, radius, intensity, timestamp)
    cursor.execute(query)
    conn.commit()
    return 0

@app.route("/testendpoint")
def testendpoint():
    return json.dumps([{
    "lat": 42.3601,
    "lng": -71.0589,
    "radius": 100.0,
    "intsy": 5
},
{
    "lat": 42.366121,
    "lng": -71.060044,
    "radius": 50.0,
    "intsy": 8
},
        {
            "lat": 42.364,
            "lng": -71.04,
            "radius": 50.0,
            "intsy": -5
        }
    ])

@app.route("/writeWifi")
def writeWifi():
    lights = [

        ]

    for element in crimecenters:
        _id = str(uuid.uuid4())
        cursor.execute("INSERT INTO crimecenters(id, lat, lon, radius) VALUES (%s, %s, %s, %s)", (_id, element[0], element[1], 50))
        conn.commit()
    result = cursor.fetchall()
    return json.dumps(result)


if __name__ == "__main__":
    app.run(host= '0.0.0.0')