txt1="El MCD entre {} y {} es:{}"
txt2="ingrese el primer número:"
txt3="ingrese el segundo número:"
txt4="Encontrar el MCD entre dos números"
print(txt4)
n1=int(input(txt2))
n2=int(input(txt3))

def MCD(a,b):
    while True:
        r=a%b
        a=b
        b=r
        if r==0:
            break
    return(txt1.format(n1,n2,a))
        
print(MCD(n1,n2))