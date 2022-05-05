# Segunda manera de crear mi estructura de datos

residentes = [
    ['Guillermo', 'Keneth', 'Elizabeth'],
    ['Pizarro', 'Vera', 'Martinez'],
    [1, 1, 3],
    [2, 5, 1],
    ['05-05-2022', '05-05-2020', '05-07-2020']
]

for i in range(0, len(residentes)):
    for j in range(0, len(residentes[i])):
        print( '{}'.format( residentes[i][j] ) )

for i in range(0, len(residentes)):
    print( '{}'.format( residentes[i][0] ) )