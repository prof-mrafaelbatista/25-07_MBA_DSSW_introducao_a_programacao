# Exercício do Tempo de Viagem: Escreva um programa
# em Python que solicite ao usuário a distância de
# uma viagem (em km) e a velocidade média (em km/h).
# Calcule o tempo de viagem em horas e exiba o resultado.

# Dados de Entrada
distancia = float(input('Distância: '))
velocidade = float(input('Velocidade: '))

# Processamento
tempo_viagem = distancia / velocidade

# Saída
print(f'O tempo de viagem é {tempo_viagem:.2f}h')