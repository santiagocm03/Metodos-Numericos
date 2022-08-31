# Método de Newton-Raphson
# Ejemplo 1 (Burden ejemplo 1 p.51/pdf.61)

import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(12,8), constrained_layout=True)
gs=fig.add_gridspec(1,1)
ax1=fig.add_subplot(gs[0,0])


# INGRESO
fx  = lambda x: np.pi*(x**2)*((3*3-x)/(3))-30
dfx = lambda x: np.pi*x*(-x+2*3)

X=np.linspace(0,100,100)
y=np.pi*(X**2)*((3*3-X)/(3))-30
x0 = 1

# PROCEDIMIENTO
data = []
xi = x0
for n in range(10):
    xnuevo = xi - fx(xi)/dfx(xi)
    error  = (abs(xnuevo-xi)/xnuevo)*100
    Lista=[n+1,xnuevo,error]
    data.append(Lista)
    if error<0.003:
        break
    xi = xnuevo

# convierte la lista a un arreglo
head=["Iteración","Aproximación","Error(%)"]
print(tabulate(data,headers=head,tablefmt="grid"))

plt.axhline(y=0, xmin=-10, xmax=10,color="k")
plt.plot(X,y)
plt.plot(xnuevo,0, marker="o", color="red")
plt.grid()
plt.show()