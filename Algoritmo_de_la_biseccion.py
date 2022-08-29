import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

fig=plt.figure(figsize=(12,8), constrained_layout=True)
gs=fig.add_gridspec(1,1)
ax1=fig.add_subplot(gs[0,0])


x=np.linspace(0.1,10,100)
y=np.exp(-x)-np.log(x)

a=1
b=2
xe=0
data=[]
for n in range(10):
    xr=(a+b)/2
    error=(abs(xr-xe)/xr)*100
    fa=np.exp(-(a))-np.log((a))
    fb=np.exp(-(b))-np.log((b))
    fa=np.exp(-(a))-np.log((a))
    fxr=np.exp(-(xr))-np.log((xr))
    if fxr*fb<0:
        a=xr
    elif fxr*fa<0:
        b=xr
    xe=xr
    lista=[n,xr,error]
    data.append(lista)
    
head=["Iteración","Aproximación","Error(%)"]
print(tabulate(data,headers=head,tablefmt="grid"))

plt.axhline(y=0, xmin=-10, xmax=10,color="k")
plt.plot(x,y)
plt.plot(xr,0, marker="o", color="red")
plt.grid()
plt.show()