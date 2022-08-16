
import matplotlib.pyplot as plt

def graficar():
    fig = plt.figure()
    fig.canvas.mpl_connect('figure_enter_event', ingresar)
    fig.canvas.mpl_connect('figure_leave_event', salir)
    fig.canvas.mpl_connect('axes_enter_event', ingresar_eje)
    fig.canvas.mpl_connect('axes_leave_event', salir_eje)
    fig.canvas.mpl_connect('button_press_event', presionar_boton)

    fig.canvas.manager.set_window_title('Ejemplo de eventos en matplotlib.')
    ax = fig.add_subplot(111)
    ax.set_title('Haz click con el raton o mueve su rueda.')
    plt.show()

def presionar_boton(event):
    if event.button == 1:
        print('Has pulsado el boton izquierdo del mouse.')
    elif event.button == 2:
        print('Has pulsado el boton central del mouse.')
    elif event.button == 3:
        print('Has pulsado el boton derecho del mouse.')
        
def ingresar_eje(event):
    print('Has ingresado al objeto Eje.')

def salir_eje(event):
    print('Has salido del objeto Eje.')

def salir(event):
    print('Has salido del objeto Figure.')

def ingresar(event):
    print('Has entrado en el objeto Figure.')

if __name__ == '__main__':
    graficar()