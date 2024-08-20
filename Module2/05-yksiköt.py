leiviskat = float(input("Anna leiviskät.\n"))
naulat = float(input("Anna naulat.\n"))
luodit = float(input("Anna luodit.\n"))

print("Massa nykymittojen mukaan:")

grammoina = luodit * 13.3 + naulat * 32 * 13.3 + leiviskat * 20 * 32 * 13.3

kilot = int(grammoina/1000)
grammat = grammoina - kilot * 1000

print("Massa nykymittojen mukaan:\n" + str(kilot) + f" kilogrammaa ja {grammat:.2f} grammaa.")