"""
szamoklista = [3, 21, 7, 63, 27]
print(max(szamoklista))
print(min(szamoklista))
szamoklista = [3, 21, 7, 63, 27]

def szelsoertek():
    min = szamoklista[0]
    max = szamoklista[0]

    for szam in szamoklista:
        if szam < min:    
            min = szam
        if szam > max:
            max = szam

    print(f"a legkisebb szam a {min}")  
    print(f"a legnagyobb szam a {max}")  
    """

#---------------------------------------------------------------------------------------------------------------------------------------------
#osszegzes tetele    
#van egy sorozat pl egy lista, tomb . Kivancsi vagyok ,hogy kiszamolja e a elejet  meg a veget

szamoklista = [3, 21, 7, 63, 9, 27]

osszeg = 0

for reszosszeg in szamoklista:
    osszeg = osszeg + reszosszeg

print(osszeg)

#a lista elemeinek atlaganak kiszamitasa

def atlagszamitas():
    atlag = None
    osszeg = 0
    for reszosszeg in szamoklista:
        osszeg = osszeg + reszosszeg
    atlag = len(szamoklista) /osszeg    
    print(f"a lista atlaga : {atlag}")
atlagszamitas()

