num1 = int(input("ingrese el primer numero"))
num2 = int(input("ingrese el segundo numero"))


for num1 in range(num1, num2+1):
    inpar = num1 % 2
    if(inpar != 0):
        print(str(num1))