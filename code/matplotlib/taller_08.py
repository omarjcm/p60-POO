from cProfile import label
import matplotlib.pyplot as plt
import numpy as np

def graficar(tamanio):
    X_ = list( range(tamanio) )
    Y1_ = [ x**0.5 for x in X_ ]
    Y2_ = [ x for x in X_ ]
    Y3_ = [ x**1.5 for x in X_ ]
    Y4_ = [ x**2 for x in X_ ]

    plt.subplot2grid((2,2),(0,0), colspan=2)
    plt.title('Cuatro funciones en un solo grafico', fontsize=14)
    plt.plot(X_, Y1_)
    plt.plot(X_, Y2_)
    plt.plot(X_, Y3_)
    plt.plot(X_, Y4_)

    plt.subplot2grid((2,2),(1,0), colspan=2)
    plt.title('Dos funciones en un solo grafico', fontsize=10)
    plt.plot(X_, Y1_, label='f(x)=x**0.5')
    plt.plot(X_, Y2_, label='f(x)=x')
    plt.grid()
    plt.legend()
    plt.annotate('f(x)=x', xytext=(1.5, 7), xy=(5.5, 5.6), 
                    ha='right', va='bottom',
                    arrowprops={'facecolor':'blue', 'shrink':0.02})
    plt.annotate('f(x)=x**0.5', xytext=(7, 5), xy=(6, 2.6), 
                    ha='center', va='center',
                    arrowprops={'arrowstyle':'->', 'color':'red'})

    plt.show()

if __name__ == '__main__':
    graficar(10)