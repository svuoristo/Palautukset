import mysql.connector
from geopy.distance import distance

connection = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='palautukset',
         password='moro3',
         autocommit=True,
         collation = "utf8mb4_general_ci",
         )

def location(airportcode):
    sql = f"SELECT latitude_deg, longitude_deg FROM Airport WHERE ident = '{airportcode}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

icao1 = input("Enter an airport's ICAO code: ")
icao2 = input("Enter another airport's ICAO code: ")

print(f"The distance is about {distance(location(icao1), location(icao2)).km:.2f} km.")

