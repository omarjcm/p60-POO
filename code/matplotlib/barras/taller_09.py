import matplotlib.pyplot as plt
import numpy as np

def graficar():
    eje_x = list(range(1, 13))
    eje_y = np.random.randint(100, size=12)

    plt.xlim(0.5, 12.5)
    plt.ylim(0, 100)
    dias = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
            'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    plt.xticks([x for x in range(1, 13)], dias, fontsize=8, rotation=25)
    plt.yticks([10*x for x in range(11)])
    plt.bar(eje_x, eje_y, color='orange', align='center', width=1)
    plt.show()

if __name__ == '__main__':
    graficar()