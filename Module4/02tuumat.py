# 1 tuuma = 2,54 cm

tuumat = 0
#tuumat = float(input("Anna tuumamitta lukuna: "))

while tuumat >= 0:
    tuumat = input("Anna tuumamitta lukuna: ")
    try:
        tuumat = float(tuumat)
    except ValueError:
        print("Tuumamitan täytyy olla luku.")
        break
    if tuumat < 0:
        break
    print(str(tuumat) + " tuumaa on " + str(tuumat * 2.54) + " senttiä.")

#        print("Not a float")
#   if tuumat != "":
#        tuumat = float(tuumat)
#    else:
#        tuumat = 0
#    if tuumat < 0:
#        break
#    print(str(tuumat) + " tuumaa on " + str(tuumat * 2.54) + " senttiä.")