import Rollers
ujRoller = Rollers.Eroller("Akai F10",25,250)
print(ujRoller.ToString())
rollerek = []
ujNev = " "
while ujNev != "":
    ujNev = input("Kérem, adja meg a következő roller márkáját: ")
    if ujNev != "":
        ujSeb = input("Kérem, adja meg a roller maximális sebességét: ")
        ujTelj = input("Kérem, adja meg a roller teljesítményét: ")
        rollerek.append(Rollers.Eroller(ujNev,ujSeb,ujTelj))
        print('Sikeres rögzítés')
with open('tobbmint500.txt', 'w', encoding='utf-8') as kimenet:
    for roller in rollerek:
        if roller.teljesitmeny > 500:
            kimenet.write(f"{roller.marka}\n")