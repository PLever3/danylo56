def plus(a, b):
	return a + b

def minus(a, b):
	return a - b
    
def mult(a, b):
    return a * b

def div(a, b):
    return a / b


while True:
    firstNumber = int(input('input first integer number: '))
    secondNumber = int(input('input second integer number: '))

    
    print(' Menu '
          '\n1 - plus',
          '\n2 - minus',
          '\n3 - mult',
          '\n4 - div',
          '\n0 - exit'
          )
    operation = input('Choose youroperation: ')
    print (operation)
    if operation == '1' :
        print(plus (firstNumber, secondNumber))
    elif operation == '2':
        print(minus (firstNumber, secondNumber))
    elif operation == '3':
        print(mult(firstNumber, secondNumber))
    elif operation == '4':
        if secondNumber == 0:
            print('второе число не может быть 0')
        else:
             print(div(firstNumber, secondNumber))
    elif operation == '0':
            break
