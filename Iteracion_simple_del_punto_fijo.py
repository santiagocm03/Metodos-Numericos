import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
x=np.linspace(0.1,10,100)
y=np.exp(-x)-np.log(x)
def g(x):
    return x+np.exp(-x)-np.log(x)
x0=1
data=[]
for n in range(11):
    x1=g(x0)
    error=((abs(x1-x0)/x1)*100)
    lista=[n,x1,error]
    data.append(lista)
    #if (abs(x1-x0)<0.000005):#en esta parte debe ingresar el valor
                              #de la tolerancia, para que funcione
                              #borre los "#" que acompañan al if y
                              #el break de las lineas 15 y 19
     #   break
    x0=x1
    
head=["Iteración","Aproximación","Error(%)"]
print(tabulate(data,headers=head,tablefmt="grid"))
plt.axhline(y=0, xmin=-10, xmax=10,color="k")
plt.plot(x,y)
plt.plot(x1,0, marker="o", color="red")
plt.grid()
plt.show()