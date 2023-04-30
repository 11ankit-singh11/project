from random import randint
r = randint(8,12)
l = []
s = '"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
la = len(s)
for i in range(0,r):
    k = randint(1,4)
    if (k==1):
        l.append(chr(randint(65,90)))
    elif (k==2):
        l.append(chr(randint(97,122)))
    elif (k==3):
        l.append(str(randint(0,9)))         
    else:
        p = randint(0,la)
        l.append(s[p])         
s = ''.join(l)
print(s)
    
