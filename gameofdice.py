from  random import randint
a = int(input("enter no. of times you want to throw dice "))
for i in range(a):
    b = randint(1,6)
    print(' -------')
    if(b==1):
        print("|       |")
        print("|   ●   |")
        print("|       |")
    elif(b==2):
        print("| ●     |")
        print("|       |")
        print("|     ● |")
    elif(b==3):
        print("| ●     |")
        print("|   ●   |")
        print("|     ● |")
    elif(b==4):
        print("| ●   ● |")
        print("|       |")
        print("| ●   ● |")
    elif(b==5):
        print("| ●   ● |")
        print("|   ●   |")
        print("| ●   ● |")
    else:
        print("| ●   ● |")
        print("| ●   ● |")
        print("| ●   ● |")
    print(" ------- ")
    print('\n\n\n')
