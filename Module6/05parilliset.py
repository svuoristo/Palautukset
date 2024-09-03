def karsiparittomat(luvut):
    parilliset = []
    for luku in luvut:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset

testi = [3, -5, -4, 110, 0, 70]

print(testi)
print(karsiparittomat(testi))