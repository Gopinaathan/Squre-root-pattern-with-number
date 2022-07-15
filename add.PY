side = int(input("Please Enter any Side of a Square  : "))
a=int(side**0.5)
num = 1
for i in range(a):
    for j in range(a):
        print(num, end = ' 5')
        num =num+ 1
    print('\n')
