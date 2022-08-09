from turtle import color
import matplotlib.pyplot as plt

def graficar():
    eje_y = list(range(1,11))
    eje_x = [25, 4, 32, 77, 8, 43, 45, 90, 12, 68]
    eje_x2 = [45, 10, 3, 7, 65, 4, 32, 21, 38, 6]
    eje_x3 = [11, 98, 42, 71, 12, 67, 4, 9, 2, 52]

    plt.ylim(0, 11)
    plt.barh(eje_y, eje_x, color='green', align='center')
    plt.barh(eje_y, eje_x2, color='blue', align='center', left=eje_x)
    plt.barh(eje_y, eje_x3, color='orange', align='center',\
                left=[eje_x[i]+eje_x2[i] for i in range(len(eje_x))])
    plt.show()

if __name__ == '__main__':
    graficar()