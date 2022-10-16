import matplotlib.pyplot as plt
import numpy as np
import sympy as sym

fig=plt.figure(figsize=(12,8), constrained_layout=True)
gs=fig.add_gridspec(1,1)
ax1=fig.add_subplot(gs[0,0])


xi=np.array([0,4,8,11,15,22])
fi=np.array([-1,5,9,-3,7,-4])



X=sym.Symbol("X")


hi=[]
for n in range(0,len(xi)-1):
    hi.append(xi[n+1]-xi[n])
    
A=np.zeros((len(xi),len(xi)))
L1=np.zeros(len(xi))    
L1[0]=1
A[0,:]=L1

for n in range(0,len(xi)-2):
        L2=np.zeros(len(xi))
        L2[n]=hi[n]
        L2[n+1]=2*(hi[n]+hi[n+1])
        L2[n+2]=hi[n+1]
        A[n+1,:]=L2
    
L3=np.zeros(len(xi))
L3[len(xi)-1]=1
A[len(xi)-1,:]=L3

Ain=np.linalg.inv(A)

b=np.zeros(len(xi))
b[0]=0
b[len(xi)-1]=0
for k in range(1,len(xi)-1):
    b[k]=((3/hi[k])*(fi[k+1]-fi[k]))-((3/hi[k-1])*(fi[k]-fi[k-1]))
    
ci=np.dot(Ain,b)
bi=np.zeros(len(xi))        
di=np.zeros(len(xi))  
        
for n in range(0,len(xi)-1):
    bi[n]=((fi[n+1]-fi[n])/hi[n])-((hi[n]*(ci[n+1]+2*ci[n]))/3)
    di[n]=(ci[n+1]-ci[n])/(3*hi[n])


for n in range(0,len(xi)-1):
    x=np.linspace(xi[n],xi[n+1],100)
    y=fi[n]+bi[n]*(x-xi[n])+ci[n]*(x-xi[n])**2+di[n]*(x-xi[n])**3
    polinomio=fi[n]+bi[n]*(X-xi[n])+ci[n]*(X-xi[n])**2+di[n]*(X-xi[n])**3
    polisimple=sym.expand(polinomio)
    print("-",polisimple)
    ax1.plot(x,y)
    plt.show()
    
ax1.plot(xi,fi,"o")
ax1.grid()