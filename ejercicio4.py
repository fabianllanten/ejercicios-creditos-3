num1 = int(input("ingrese el primer numero"))
num2 = int(input("ingrese el segundo numero"))


print("la suma de los dos numeros es "+str(int(num1+num2)))
print("la resta de los dos numeros es "+str(int(num1-num2)))
print("la multiplicacion de los dos numeros es "+str(int(num1*num2)))

if num2 == 0:
    print("no es posible dividir entre cero")
else:
    print("la division de los dos numeros es "+str(int(num1/num2)))