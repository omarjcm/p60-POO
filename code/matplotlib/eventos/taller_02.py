import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

fig = plt.figure()

def graficar():
    fig.canvas.mpl_connect('button_press_event', presionar_boton)

    fig.canvas.manager.set_window_title('Ejemplo de eventos en matplotlib.')

    numeros, frecuencias = obtener_datos()
    plt.bar(numeros, frecuencias)
    plt.show()

def obtener_datos():
    numeros = np.random.randint(30, size=(1000))
    frecuencias = Counter(numeros)

    num_ = frecuencias.keys()
    frec_ = frecuencias.values()

    return (num_, frec_)

def presionar_boton(event):
    if event.button == 1:
        numeros, frecuencias = obtener_datos()
        frecuencias = sorted(frecuencias)
        plt.clf()
        plt.bar(numeros, frecuencias)
        fig.canvas.draw()
    elif event.button == 3:
        numeros, frecuencias = obtener_datos()
        plt.clf()
        plt.bar(numeros, frecuencias)
        fig.canvas.draw()

if __name__ == '__main__':
    graficar()