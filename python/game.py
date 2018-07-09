import random
a = random.randint(10000, 99999)
print('1 num =', int((a%100000)/10000))
print('2 num =', int((a%10000)/1000))
print('3 num =', int((a%1000)/100))
print('4 num =', int((a%100)/10))
print('1 num =', int((a%10)))
c = int(input('введите число :'))
if(a == c):
    print('OK')
else:
    print('ERROR')
