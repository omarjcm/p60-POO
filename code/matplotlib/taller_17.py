import matplotlib.pyplot as plt

def graficar():
    carreras = ['Computacion', 'Sistemas']
    porcentajes = [90, 10]

    plt.pie(porcentajes, labels=carreras, shadow=True, labeldistance=0.7)
    plt.show()

if __name__ == '__main__':
    graficar()