import numpy as np
import matplotlib.pyplot as plt

def serieFourierCuadrada(s, r, n):
    #s = float(input("Ingresa el valor de s: "))
    #r = float(input("Ingresa el valor de r: "))
    #n = int(input("Ingresa el valor de n: "))

    impares = [x for x in range(0,n+1) if x%2 == 1]
    #print(impares)

    t = np.arange(-8*s,8*s+0.01, 0.01)

    #print(t)

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
    #print("Total: ",ft)

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
    #plt.title(r'f(t) = $\frac{-4}{\pi} \sum_{i=1}^\infty \frac{%.2f}{n}sin(\frac{nt}{%.2f})$' % (r, s))
    plt.title(r'f(t) = $\frac{-4}{\pi} ( \frac{%.2f}{1}sin(\frac{πt}{%.2f}) + \frac{%.2f}{3}sin(\frac{3πt}{%.2f}) + \frac{%.2f}{5}sin(\frac{5πt}{%.2f}) + \frac{%.2f}{7}sin(\frac{7πt}{%.2f}) + \frac{%.2f}{9}sin(\frac{9πt}{%.2f}) + \frac{%.2f}{11}sin(\frac{11πt}{%.2f}) + ... )$ ' % (r, s, r, s, r, s, r, s, r, s, r, s))
    plt.show()

def serieFourierTriangular(s, r, n):
    #s = float(input("Ingresa el valor de s: "))
    #r = float(input("Ingresa el valor de r: "))
    #n = int(input("Ingresa el valor de n: "))

    impares = [x for x in range(0,n+1) if x%2 == 1]
    #print(impares)

    t = np.arange(-8*s,8*s+0.01, 0.01)

    #print(t)

    #Calcula la serie.
    for i in range(0, len(impares)):

        if i == 0:
            ft = np.cos((impares[i]*np.pi*t)/s)        
            ft*=(1/impares[i]**2)
        else:
            ftAux = np.cos((impares[i]*np.pi*t)/s)
            ftAux*=(1/impares[i]**2)
            ft+=ftAux

    ft*=(-4*r/np.pi**2)
    ft+=r/2
    #print("Total: ",ft)

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
    plt.title(r'f(t) = $ \frac{%.2f}{2} + \frac{-4(%.2f)}{π^{2}} ( \frac{1}{1^{2}}cos(\frac{πt}{%.2f}) + \frac{1}{3^{2}}cos(\frac{3πt}{%.2f}) + \frac{1}{5^{2}}cos(\frac{5πt}{%.2f}) + \frac{1}{7^{2}}cos(\frac{7πt}{%.2f}) + \frac{1}{9^{2}}cos(\frac{9πt}{%.2f}) + \frac{1}{11^{2}}sin(\frac{11πt}{%.2f}) + ... )$ ' % (r, r, s, s, s, s, s, s))
    plt.show()

#print("1.-Serie Fourier funcion Cuadrada")
#print("2.-Serie Fourier funcion Triangular")
#opcion = int(input("Opcion: "))

#if(opcion == 1):
#    SerieFourierCuadrada()
#else:
#    SerieFourierTriangular()
