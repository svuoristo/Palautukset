import mysql.connector

connection = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='palautukset',
         password='moro3',
         autocommit=True,
         collation = "utf8mb4_general_ci",
         )

isocountry = input("Anna maakoodi: ")

amounts = f"SELECT type, COUNT(*) FROM Airport WHERE iso_country = '{isocountry}' GROUP BY type"

cursor = connection.cursor()
cursor.execute(amounts)
result = cursor.fetchall()

for row in result:
    print(f"{row[0].replace('_',' ')}: {row[1]}")
