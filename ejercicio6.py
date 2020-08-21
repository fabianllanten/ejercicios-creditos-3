num = int(1)
dem = int(1)
for num in range(1, 11):
    print("TABLA DEL "+str(num))
    for dem in range(1, 11):
        resul = num*dem
        print(str(num)+" * " + str(dem)+" = "+str(resul))