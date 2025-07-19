print('--- Iniciando o Programa ---')

temperatura = float(input('Informe a temperatura: '))

print('1 - Celsius')
print('2 - Fahrenheit')
escala = int(input('Digite a escala: '))

if escala == 1:
    #Transformar de Celsius para Fahrenheit
    temp = temperatura * 1.8 + 32
    print(f'A temperatura {temperatura} em Celsius')
    print(f'Ficou {temp} em Fahrenheit')

elif escala == 2:
    #Transforma de Fahrenheit para Celsius
    temp = (temperatura - 32) / 1.8
    print(f'A temperatura {temperatura} em Fahrenheit')
    print(f'Ficou {temp} em Celsius')

else:
    print(f'A opção {escala} é inválida!')





print('--- Programa Finalizado---')