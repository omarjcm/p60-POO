import matplotlib.pyplot as plt
import numpy as np

def graficar(tamanio):
    X_ = list( range(tamanio) )
    Y1_ = [ x**0.5 for x in X_ ]
    Y2_ = [ x for x in X_ ]
    Y3_ = [ x**1.5 for x in X_ ]
    Y4_ = [ x**2 for x in X_ ]

    plt.title('Cuatro funciones en un solo grafico', fontsize=24)
    plt.plot(X_, Y1_)
    plt.plot(X_, Y2_)
    plt.plot(X_, Y3_)
    plt.plot(X_, Y4_)
    plt.show()

if __name__ == '__main__':
    graficar(100)