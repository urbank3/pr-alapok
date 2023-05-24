import Rollers
objektum_nevek = Rollers.Eroller("AKAI F10",25.,50)
print(f"{objektum_nevek.ToString()}")

roller_nev = input=("Kérem a Roller nevét:")
rollers_max_bs = int(input("Kérem a Roller max sebességét:"))
roller_telj = int(input("Kérem a roller teljesítményét:"))

eroller1 = Rollers.Eroller(roller_nev,rollers_max_bs,roller_telj)
print(eroller1.ToString())