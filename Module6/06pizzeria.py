import math

def prezzoalmetro(prezzo, diametro):
    raggiometri = diametro / 2 / 100
    return prezzo / (raggiometri ** 2 * math.pi)

prezzo1 = float(input("Indicare il prezzo della pizza prima (€): "))
diametro1 = float(input("Indicare il diametro della pizza prima (cm): "))

prezzo2 = float(input("Indicare il prezzo della pizza seconda (€): "))
diametro2 = float(input("Indicare il diametro della pizza seconda (cm): "))

#print(f"{(prezzoalmetro(prezzo1, diametro1)):.2f} vs {(prezzoalmetro(prezzo2, diametro2)):.2f} kg/m^2.")

if prezzoalmetro(prezzo1, diametro1) < prezzoalmetro(prezzo2, diametro2):
    print("Pizza prima (1.) e piu economica.")
elif prezzoalmetro(prezzo1, diametro1) > prezzoalmetro(prezzo2, diametro2):
    print(f"Pizza seconda (2.) e piu economica.")
else:
    print("Le pizze sono altrettanto costose.")