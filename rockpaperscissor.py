from random import randint
di = {1:'rock',2:'paper',3:'scissor'}
while True:
    a = randint(1,3)
    b = input('enter rock , paper or scissor ')
    print('choice of computer is' , di[a]) 
    if di[a]==b:
        print('draw')
    elif b.lower()=='rock' and a==3:
        print('you win')
    elif b.lower()=='paper'and a==1:
        print('you win')
    elif b.lower()=='scissors'and a==2:
        print('you win')
    else:
        print('you lose')
    if input('enter y to play again and n to quit ').lower()== 'n':
        break
print('thank you')
