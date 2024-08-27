pituus = float(input("Anna kuhan pituus sentteinä ilman yksikköä: "))

if pituus < 37:
    print("Kuha on " + str(37 - pituus) + " cm liian lyhyt. Päästä kuha vapaaksi.")
else:
    print("Onnea! Nappasit oivan kuhan.")