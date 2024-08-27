yritykset = 0

while yritykset < 5:
    k_oikein = input("Käyttajatunnus: ") == "python"
    s_oikein = input("Salasana: ") == "rules"
    if k_oikein and s_oikein:
        yritykset = 5
        print("Tervetuloa")
    else:
        yritykset += 1
        if yritykset == 5:
            print("Pääsy evätty.")

