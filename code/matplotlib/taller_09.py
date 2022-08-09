import matplotlib.pyplot as plt
import numpy as np

def graficar(tamanio):
    x = np.random.randint(10, size=tamanio)
    y = np.random.randint(10, size=tamanio)

    plt.scatter(x, y)
    plt.show()

if __name__ == '__main__':
    graficar(100)