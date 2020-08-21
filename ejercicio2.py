numero = int(1)

for numero in range(1, 121):
    par = numero % 2
    if(par == 0):
        print(str(numero))