import mysql.connector
from flask import Flask, Response
import json

connection_thing = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='palautukset',
    password='moro3',
    autocommit=True,
    collation="utf8mb4_general_ci",
)

app = Flask(__name__)
@app.route('/kenttä/<icao>')
def airport(icao):
    sql = f"SELECT Name, Municipality FROM Airport WHERE ident = '{icao}'"
    cursor_thing = connection_thing.cursor()
    cursor_thing.execute(sql)
    result = cursor_thing.fetchall()

    if cursor_thing.rowcount > 0:
        name = ''
        municipality = ''
        status_code = 200
        for row in result:
            name = row[0]
            municipality = row[1]
        response = {
            "ICAO": icao,
            "Name": name,
            "Municipality": municipality
        }
    else:
        status_code = 400
        response = {
            "status": status_code,
            "message": "ICAO was not found"
        }

    json_response = json.dumps(response)
    return Response(response=json_response, status=status_code, mimetype='application/json')

@app.errorhandler(400)
def page_not_found(error):
    response = {
        "status": 400,
        "message": "Bad Request"
    }
    json_response = json.dumps(response)
    return Response(response=json_response, status=error, mimetype='application/json')

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)