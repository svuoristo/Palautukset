def litroiksi(gallonat):
    litrat = gallonat * 3.785
    return litrat

syotegallonat = float(input("Anna bensiinin määrä Yhdysvaltain nestegallonoina: "))

while syotegallonat >= 0:
    print(litroiksi(syotegallonat))
    syotegallonat = float(input("Anna bensiinin määrä Yhdysvaltain nestegallonoina: "))