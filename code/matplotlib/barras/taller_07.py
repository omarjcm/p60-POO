import matplotlib.pyplot as plt

def graficar():
    eje_x = list(range(1,11))
    eje_x2 = [x + 1/3 for x in eje_x]
    eje_x3 = [x + 2/3 for x in eje_x]

    eje_y = [23, 4, 32, 77, 8, 43, 45, 90, 12, 68]
    eje_y2 = [45, 10, 3, 7, 65, 4, 32, 21, 38, 6]
    eje_y3 = [11, 98, 42, 71, 12, 67, 4, 9, 2, 52]

    plt.xlim(1-1/16, 11-1/16)
    plt.ylim(0, 100)
    plt.grid(linestyle='--', axis='y')
    plt.bar(eje_x, eje_y, width=1/3, color='g', align='center')
    plt.bar(eje_x2, eje_y2, width=1/3, color='b', align='center')
    plt.bar(eje_x3, eje_y3, width=1/3, color='y', align='center')
    plt.show()

if __name__ == '__main__':
    graficar()