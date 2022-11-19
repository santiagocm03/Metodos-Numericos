import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d



a=10
b=28
s=8/3

t0=0
x0=2
y0=1
z0=1

tf=40
n=100000
h=(tf-t0)/n


def dx(x,y,z):
    return a*(y-x)
def dy(x,y,z):
    return x*(b-z)-y
def dz(x,y,z):
    return x*y-s*z
X=[x0]
Y=[y0]
Z=[z0]
for i in range(0,n):
    k1=dx(x0,y0,z0)
    L1=dy(x0,y0,z0)
    m1=dz(x0,y0,z0)
    xi=x0+k1*h
    yi=y0+L1*h
    zi=z0+m1*h
    X.append(xi)
    Y.append(yi)
    Z.append(zi)
    x0=xi
    y0=yi
    z0=zi

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(X,Y,Z)
plt.show()