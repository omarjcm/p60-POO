import matplotlib.pyplot as plt
import numpy as np

def graficar(tamanio):
    X_ = list( range(tamanio) )
    Y1_ = [ 1/(x+5) for x in X_ ]
    Y2_ = [ x**2 for x in X_ ]
    Y3_ = [ ((x-2)/(x+1))**0.5 for x in X_ ]

    plt.subplot2grid((2,2), (0,0), rowspan=1)
    plt.plot(X_, Y1_)
    plt.subplot2grid((2,2), (0,1), rowspan=1)
    plt.plot(X_, Y2_)
    plt.subplot2grid((2,2), (1,0), colspan=2)
    plt.plot(X_, Y3_)
    plt.show()

if __name__ == '__main__':
    graficar(50)