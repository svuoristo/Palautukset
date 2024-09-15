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

airport1 = input("Enter an airport's ICAO code: ")
airport2 = input("Enter another airport's ICAO code: ")

print(f"The distance is about {distance(location(airport1), location(airport2)).km:.2f} km.")



# if you want to include the names of the airports:
'''
def name(airportcode):
    sql = f"SELECT name FROM Airport WHERE ident = '{airportcode}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return (result[0])[0]

try:
    print(f"The distance between "
          f"{name(airport1)} and {name(airport2)} is about "
          f"{distance(location(airport1), location(airport2)).km:.2f} "
          f"km.")
except IndexError:
    print("No airports found.") 
'''