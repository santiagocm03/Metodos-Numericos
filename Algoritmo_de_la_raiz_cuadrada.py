from tabulate import tabulate
import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(12,8), constrained_layout=True)
gs=fig.add_gridspec(1,1)
ax1=fig.add_subplot(gs[0,0])

z=np.linspace(0,10,100)
y=np.sqrt(z)



txt1="Algoritmo de la raiz cuadrada"
txt2="ingrese el numero de aproximaciones que desea:"

n=int(input(txt2))

a=5 #este numero corresponde al cual se quiere encontrar su raiz
        #para el ejercicio propuesto es el 5
x_0=2 #valor inicial propuesto en clase, tambien se propuso 10
          #reemplazar este valor en la variable x_0
data=[]

for N in range(n):
    contador=N+1
    x=(1/2)*(x_0+(a/x_0))
    e=(abs(x-x_0)/x)*100
    lista=[contador,x,e]
    data.append(lista)
    if x_0==x:
        break
    x_0=x

head=["Iteración","Aproximación","Error(%)"]
print(tabulate(data,headers=head,tablefmt="grid"))
ax1.plot(z,y)

plt.show()



