import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

def graficar_barras(tamanio):
    numeros = np.random.randint(100, size=(tamanio))
    frecuencias = Counter(numeros)

    num_ = list(frecuencias.keys())
    frec_ = list(frecuencias.values())

    plt.subplot2grid((1,2), (0,0), rowspan=1, colspan=1)
    plt.xlim(0,50)
    plt.ylim(0,4)
    plt.bar(num_, frec_)
    plt.subplot2grid((1,2), (0,1), rowspan=1, colspan=1)
    plt.xlim(0,4)
    plt.ylim(0,50)
    plt.barh(num_, frec_)
    plt.show()
    
if __name__ == '__main__':
    graficar_barras(50)