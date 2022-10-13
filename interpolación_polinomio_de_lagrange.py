import matplotlib.pyplot as plt
import numpy as np
import sympy as sym

fig=plt.figure(figsize=(12,8), constrained_layout=True)
gs=fig.add_gridspec(1,1)
ax1=fig.add_subplot(gs[0,0])

xi=np.array([0,0.2,0.3,0.4])
fi=np.array([1,1.6,1.7,2])


n=len(xi)
x=sym.Symbol("x")
polinomio=0
for i in range(0,n,1):    
    numerador=1
    denominador=1
    for j in range(0,n,1):
        if i!=j:
            numerador=numerador*(x-xi[j])
            denominador=denominador*(xi[i]-xi[j])
        termino=(numerador/denominador)*fi[i]
    polinomio=polinomio+termino
polisimple=sym.expand(polinomio)
px=sym.lambdify(x,polinomio)

muestras=50
a=np.min(xi)
b=np.max(xi)
p_xi=np.linspace(a,b,muestras)
pfi=px(p_xi)


print("polinomio:")
print(polinomio)
print("polinomio simplificado:")
print(polisimple)

ax1.plot(xi,fi,"o")
ax1.plot(p_xi,pfi)
plt.grid()
plt.show() 

