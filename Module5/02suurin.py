
luku = input("Anna luku tai päätä syötteen antaminen painamalla enter: ")
luvut = []

while luku != "":
    luvut.append(float(luku))
    luku = input("Anna luku tai päätä syötteen antaminen painamalla enter: ")
    luvut.sort(reverse=True)

if len(luvut) < 5:
    for n in range(len(luvut)):
        print(luvut[n])
else:
    for n in range(5):
        print(luvut[n])