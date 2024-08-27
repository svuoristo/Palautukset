sukupuoli = input('Anna biologinen sukupuoli muodossa "n"/"m": ')
hemoglobiini = input('Anna hemoglobiiniarvo (g/l): ')

if sukupuoli == 'n':
    if float(hemoglobiini) < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif float(hemoglobiini) > 175:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")
elif sukupuoli == 'm':
    if float(hemoglobiini) < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif float(hemoglobiini) > 195:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")
else:
    print('Sukupuoli täytyy antaa muodossa "n"/"m". ')
