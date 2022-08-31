# Método de Newton-Raphson
# Ejemplo 1 (Burden ejemplo 1 p.51/pdf.61)

import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(12,8), constrained_layout=True)
gs=fig.add_gridspec(1,1)
ax1=fig.add_subplot(gs[0,0])


def f(x):
    return  np.pi*(x**2)*((3*3-x)/(3))-30


X=np.linspace(0,100,100)
y=np.pi*(X**2)*((3*3-X)/(3))-30

x1=1
x0=2

# PROCEDIMIENTO
data = []
xi = x0
xi1=x1
for n in range(10):
    xnuevo = xi - ((f(xi)*(xi1-xi))/(f(xi1)-f(xi)))
    error  = (abs(xnuevo-xi)/xnuevo)*100
    Lista=[n+1,xnuevo,error]
    data.append(Lista)
    if error<0.003:
        break
    xi1=xi
    xi = xnuevo

# convierte la lista a un arreglo
head=["Iteración","Aproximación","Error(%)"]
print(tabulate(data,headers=head,tablefmt="grid"))

plt.axhline(y=0, xmin=-10, xmax=10,color="k")
plt.plot(X,y)
plt.plot(xnuevo,0, marker="o", color="g")
plt.grid()
plt.show()
