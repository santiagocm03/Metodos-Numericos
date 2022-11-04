import numpy as np
import matplotlib.pyplot as plt
texto="con {} tramos la integral es:{}"

f=lambda x:np.log(x)
a=1
b=5
tramos=6

muestras=tramos+1
suma=0
h=(b-a)/tramos
xi=a
for i in range(0,tramos,1):
    AreaT=h*(f(xi)+f(xi+h))/2
    suma+=AreaT
    xi=xi+h
integral=suma

xi=np.linspace(a,b,muestras)
fi=f(xi)


muestraslinea=muestras*10
xk=np.linspace(a,b,muestraslinea)
fk=f(xk)

print(texto.format(tramos,integral))
plt.plot(xk,fk,"k")
plt.plot(xi,fi,"ro")
plt.fill_between(xi,0,fi,color="red")
for i in range(0,muestras,1):
    plt.axvline(xi[i],color="w")
plt.show()