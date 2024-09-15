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

def location(icao):
    sql = f"SELECT name, latitude_deg, longitude_deg FROM Airport WHERE ident = '{icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            result = row[0], (row[1], row[2])
    else:
        result = None
    return result


airport1 = location(input("Enter an airport's ICAO code: "))
airport2 = location(input("Enter another airport's ICAO code: "))


if (airport1 or airport2) is None:
    print("Couldn't find neither airport.")
elif airport1 is None:
    print("Couldn't find the first airport.")
elif airport2 is None:
    print("Couldn't find the second airport.")
else:
    print(
        f"The distance between "
        f"{airport1[0]} and "
        f"{airport2[0]} is about "
        f"{distance(airport1[1], airport2[1]).km:.2f} km."
    )
