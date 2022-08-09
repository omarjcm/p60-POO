from turtle import color
import matplotlib.pyplot as plt

def graficar():
    eje_x = list(range(1,11))
    eje_y = [25, 4, 32, 77, 8, 43, 45, 90, 12, 68]
    eje_y2 = [45, 10, 3, 7, 65, 4, 32, 21, 38, 6]

    plt.xlim(0, 11)
    plt.ylim(0, 120)
    plt.bar(eje_x, eje_y, color='green', align='center')
    plt.bar(eje_x, eje_y2, color='blue', align='center', bottom=eje_y)
    plt.show()

if __name__ == '__main__':
    graficar()