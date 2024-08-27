vuosi = int(input("Anna vuosiluku: "))

if vuosi % 100 == 0 and vuosi % 400 != 0:
    print("Vuosi " + str(vuosi) + " ei ole karkausvuosi.")
elif vuosi % 4 == 0:
    print("Vuosi " + str(vuosi) + " on karkausvuosi.")
else:
    print("Vuosi " + str(vuosi) + " ei ole karkausvuosi.")