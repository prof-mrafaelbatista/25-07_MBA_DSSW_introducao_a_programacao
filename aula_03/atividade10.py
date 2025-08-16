from random import randint
import time

numero_aleatorio = randint(1, 100)
parada = True

while parada:

    meu_numero = int(input('Digite um numero 1-100: '))

    if meu_numero == numero_aleatorio:
        print('Você acertou!')
        parada = False

    elif meu_numero < numero_aleatorio:
        print('Seu número é MENOR!')
        print('Tente um número MAIOR')

    elif meu_numero > numero_aleatorio:
        print('Seu número é MAIOR!')
        print('Tente um número MENOR')

    time.sleep(1)


print('Programa encerrado!')