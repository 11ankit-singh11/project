from random import randint
k = randint(0,9)
a = int(input('enter a number 0-9\n'))
score = 0
if k==a :
    print('Right guess')
else:
    print('wrong guess')    
while a!=k :
    score = score + 1
    a = int(input('enter a number again\n'))
    if a==k:
        print('right guess')
        break
    else:
        print('wrong guess')
print('your score is ',score )     
