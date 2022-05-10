residentes = [
    [1, 'Guillermo', 'Pizarro', 1, 2, '05-05-2022'],
    [2, 'Keneth', 'Vera', 1, 5, '05-05-2020'],
    [3, 'Elizabeth', 'Martinez', 3, 1, '05-07-2022']
]

residentes.append( [4, 'Steven', 'Baque', 2, 3, '05-07-2019'] )
residentes.append( [len(residentes)+1, 'Alexander', 'Leon', 2, 4, '05-07-2021'] )

# Modificar el primer elemento
#residentes[0] = [1, 'Alexander', 'Leon', 2, 4, '05-07-2021']
#residentes[0][1] = 'Leon Laborda'

# Elimimar el primer elemento
#del residentes[0]

for i in range(0, len(residentes)):
    print( residentes[i][5] )

