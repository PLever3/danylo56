import time
import os
def cls():
    os.system('cls')
while True:
    cls()
    print(' Menu ',
                '\n1 - пятизначные ',
                '\n2 - шестизначные ',
                '\n3 - семизначные',
                '\n4 - восьмизначные',
                  )
    operation = input('Choose youroperation: ')
    print (operation)
    if operation == '1' :
            import random
            a = random.randint(10000, 99999)
            print('1 num =', int((a%100000)/10000))
            time.sleep(2)
            print('2 num =', int((a%10000)/1000))
            time.sleep(2)
            print('3 num =', int((a%1000)/100))
            time.sleep(2)
            print('4 num =', int((a%100)/10))
            time.sleep(2)
            print('1 num =', int((a%10)))
            time.sleep(2)
            c = int(input('введите число :'))
            if(a == c):
                print('CORRECT')
            else:
                print('INCORRECT')
    elif operation == '2':
            import random
            a = random.randint(100000, 999999)
            print('1 num =', int((a%1000000)/100000))
            time.sleep(2)
            print('2 num =', int((a%100000)/10000))
            time.sleep(2)
            print('3 num =', int((a%10000)/1000))
            time.sleep(2)
            print('4 num =', int((a%1000)/100))
            time.sleep(2)
            print('5 num =', int((a%100)/10))
            time.sleep(2)
            print('6 num =', int((a%10)))
            time.sleep(2)
            c = int(input('введите число :'))
            if(a == c):
                print('CORRECT')
            else:
                print('INCORRECT')
    elif operation == '3':
            import random
            a = random.randint(1000000, 9999999)
            print('1 num =', int((a%10000000)/1000000))
            time.sleep(2)
            print('2 num =', int((a%1000000)/100000))
            time.sleep(2)
            print('3 num =', int((a%100000)/10000))
            time.sleep(2)
            print('4 num =', int((a%10000)/1000))
            time.sleep(2)
            print('5 num =', int((a%1000)/100))
            time.sleep(2)
            print('6 num =', int((a%100)/10))
            time.sleep(2)
            print('7 num =', int((a%10)))
            time.sleep(2)
            c = int(input('введите число :'))
            if(a == c):
                print('CORRECT')
            else:
                print('INCORRECT')
    elif operation == '4':
            import random
            a = random.randint(10000000, 99999999)
            print('1 num =', int((a%100000000)/10000000))
            time.sleep(2)
            print('2 num =', int((a%10000000)/1000000))
            time.sleep(2)
            print('3 num =', int((a%1000000)/100000))
            time.sleep(2)
            print('4 num =', int((a%100000)/10000))
            time.sleep(2)
            print('5 num =', int((a%10000)/1000))
            time.sleep(2)
            print('6 num =', int((a%1000)/100))
            time.sleep(2)
            print('7 num =', int((a%100)/10))
            time.sleep(2)
            print('8 num =', int((a%10)))
            time.sleep(2)
            c = int(input('введите число :'))
            if(a == c):
                print('CORRECT')
            else:
                print('INCORRECT')

