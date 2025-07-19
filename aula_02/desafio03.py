peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura**2)

if imc < 18.5:
    print('Abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Peso normal!')
elif 25 <= imc < 30:
    print('Sobrepeso!')
elif 30 <= imc < 35:
    print('Obesidade Grau I')
elif 35 <= imc < 40:
    print('Obesidade Grau II')
elif 40 <= imc:
    print('Obesidade Grau III')

print(f'O IMC foi de {imc:.2f}')