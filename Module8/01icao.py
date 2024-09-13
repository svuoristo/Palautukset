import mysql.connector

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='palautukset',
         password='moro3',
         autocommit=True,
         collation = "utf8mb4_general_ci",
         )

icao = input("Anna lentoaseman ICAO-koodi: ")

sql = f"SELECT Name, Municipality FROM Airport WHERE ident = '{icao}'"
print(sql)
kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()

if kursori.rowcount >0 :
    for rivi in tulos:
        print(f"Kentän {rivi[0]} kunta on {rivi[1]}.")