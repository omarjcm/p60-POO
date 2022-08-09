import matplotlib.pyplot as plt
import numpy as np

def graficar(tamanio):
    # obtener 20 numeros aleatorios del 1 al 10. 
    x = np.random.randint(10, size=tamanio)
    x = np.sort(x)
    # 
    y = np.random.uniform(1, 100, size=tamanio)
    y = np.sort(y)

    plt.plot(x, y)
    plt.show()

if __name__ == '__main__':
    graficar(100)