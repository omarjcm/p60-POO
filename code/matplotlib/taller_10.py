import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

def graficar_barras(tamanio):
    numeros = np.random.randint(100, size=(tamanio))
    frecuencias = Counter(numeros)

    num_ = frecuencias.keys()
    frec_ = frecuencias.values()

    plt.bar(num_, frec_)
    plt.show()
    
if __name__ == '__main__':
    graficar_barras(1000)