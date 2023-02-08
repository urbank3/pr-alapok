#van egy N elemu lista sorozat . A sorozatban van egy T tulajdonsag. Es az algoritmusom megadja nekem ,hogy van-e a listaban ,ilyen T tuladjonsagu elem.(igen, vagy nem)

lista=[2,5,4,8,19,11,10,13]
talalat = False
index = 0
while index < len(lista) and not talalat:
        if lista[index] % 3 == 0:
            talalat = True
        index = index + 1
    
if talalat:
        print('Van a listában hárommal osztható szám.')
else:
        print('Nincs a listában hárommal osztható szám.')