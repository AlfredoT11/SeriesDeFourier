import numpy as np
import matplotlib.pyplot as plt

def SerieFourierCuadrada():
    s = float(input("Ingresa el valor de s: "))
    r = float(input("Ingresa el valor de r: "))
    n = int(input("Ingresa el valor de n: "))

    impares = [x for x in range(0,n+1) if x%2 == 1]
    print(impares)

    t = np.arange(-8*s,8*s+0.01, 0.01)

    print(t)

    #Calcula la serie.
    for i in range(0, len(impares)):

        if i == 0:
            ft = np.sin((impares[i]*np.pi*t)/s)        
            ft*=(r/impares[i])
        else:
            ftAux = np.sin((impares[i]*np.pi*t)/s)
            ftAux*=(r/impares[i])
            ft+=ftAux

    ft*=(-4/np.pi)
    print("Total: ",ft)

    line, = plt.plot(t, ft, lw=2)

    #Muestra los ejes xy.
    ax = plt.subplot()
    ax.spines['left'].set_position('zero')

    ax.spines['right'].set_color('none')
    ax.yaxis.tick_left()

    ax.spines['bottom'].set_position('zero')

    ax.spines['top'].set_color('none')
    ax.xaxis.tick_bottom()

    #Añade estilo a la representación de la gráfica.
    plt.ylim(-r-1, r+1)
    plt.grid(True)
    plt.axis('equal')
    plt.show()

SerieFourierCuadrada()