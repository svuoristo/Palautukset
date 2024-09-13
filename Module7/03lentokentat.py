airports = {}


options = 'Kirjoita "uusi" luodaksesi uuden lentokentän, "hae" hakeaksesi jo olemassa olevan lentokentän nimen tai "lopeta" sulkeaksi ohjelman.\n'

selected = input(options)

while selected != 'lopeta':
    if selected == 'uusi':
        code = input("Anna lentokentän ICAO-koodi: ")
        name = input("Anna lentokentän nimi: ")
        airports[code] = name
        selected = input(options)

    elif selected == 'hae':
        code = input("Anna lentokentän ICAO-koodi: ")
        if code in airports.keys():
            print(f"Lentokenttä {code} on nimeltään {airports[code]}.")
        else:
            print("Lentokenttää ei löytynyt.")
        selected = input(options)

    else:
        selected = input(options)

