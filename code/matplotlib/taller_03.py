import matplotlib.pyplot as plt
import numpy as np

def graficar(tamanio):
    X_ = list( range(tamanio) )
    Y_ = [ 1/(x+5) for x in X_ ]

    plt.plot(X_, Y_)
    plt.show()

if __name__ == '__main__':
    graficar(50)