#a szélsőérték meghatározása (min max) keresése

lista =[12,5,4,8,9,11,10,12,6]


def szélsőérték_10c(munka_lista):
    min = munka_lista[0]
    max = munka_lista[0]

    for szam in munka_lista:
            if szam < min:
                min = szam
            if szam > max:
                max = szam   

    print(f"a legkisebb szam a listaban {min}")    
    print(f"a legnagyobb szam a listaban {max}")
   

szélsőérték_10c(lista)


