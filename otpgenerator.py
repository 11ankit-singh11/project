from random import randint
s = [ ]
for i in range(0,4):
    a = randint(0,9)
    s.append(str(a))
print('your OTP is ',''.join(s))   
