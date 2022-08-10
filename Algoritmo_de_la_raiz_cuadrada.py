txt1="Algoritmo de la raiz cuadrada"
txt2="ingrese el numero de aproximaciones que desea:"
n=int(input(txt2))

a=5 #este numero corresponde al cual se quiere encontrar su raiz
        #para el ejercicio propuesto es el 5
x_0=2 #valor inicial propuesto en clase, tambien se propuso 10
          #reemplazar este valor en la variable x_0
for N in range(n):

    x=(1/2)*(x_0+(a/x_0))
    if x_0==x:
        break
    x_0=x
    print(x)
    