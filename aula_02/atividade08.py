num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

if num2 > num1:
    print(f'O número {num2} é maior do que {num1}')
elif num1 > num2:
    print(f'O número {num1} é maior do que {num2}')
else:
    print('Os números são iguais!')