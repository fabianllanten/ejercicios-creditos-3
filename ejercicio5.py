num1 = int(input("ingrese el primer valor"))
num2 = int(input("ingrese el segundo valor"))

for num1 in range(num1, num2+1):
    print(str(num1))
    num1 += int(num1)