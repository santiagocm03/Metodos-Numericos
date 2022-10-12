
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt



fig=plt.figure(figsize=(12,8), constrained_layout=True)
gs=fig.add_gridspec(1,1)
ax1=plt.axes(projection="3d")


u  = lambda x,y: x**2+x*y-10
v = lambda x,y: y+3*x*y**2-57
dux= lambda x,y:2*x+y
duy= lambda x,y: x
dvx= lambda x,y: 3*y**2
dvy=lambda x,y: 1+6*x*y


x0 = 1
y0 = 1.5

data = []
xi = x0
yi = xi
for n in range(10):
    xnuevo = xi + ((v(xi,yi)*duy(xi,yi)-u(xi,yi)*dvy(xi,yi))/(dux(xi,yi)*dvy(xi,yi)-duy(xi,yi)*dvx(xi,yi)))
    ynuevo = yi + ((u(xi,yi)*dvx(xi,yi)-v(xi,yi)*dux(xi,yi))/(dux(xi,yi)*dvy(xi,yi)-duy(xi,yi)*dvx(xi,yi)))
    errorx=(abs((xnuevo-xi)/xnuevo))*100
    errory=(abs((ynuevo-yi)/xnuevo))*100
    Lista=[n+1,xnuevo,ynuevo,errorx,errory]
    data.append(Lista)
    if errorx<0.001 and errory<0.001:
        break
    xi = xnuevo
    yi = ynuevo


head=["Iteración","Aproximación x","aproximación y","error x","error y"]
print(tabulate(data,headers=head,tablefmt="grid"))

ax1.scatter(xi,yi,0,color="g")
a=b=np.arange(-10,10,0.05)
X,Y=np.meshgrid(a,b)
zs = np.array([u(a,b) for a,b in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)
zs2 = np.array([v(a,b) for a,b in zip(np.ravel(X), np.ravel(Y))])
Z2 = zs2.reshape(X.shape)

ax1.plot_surface(X, Y, Z,alpha=0.5)
ax1.plot_surface(X, Y, Z2,alpha=0.5)
