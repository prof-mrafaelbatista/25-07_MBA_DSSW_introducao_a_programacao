# Variáveis
valor_produto = float(input('Digite o valor do produto: '))
desconto = float(input('Digite o valor do desconto: '))

# Funções e Métodos

# Processamento
valor_desconto = (valor_produto * desconto) / 100
valor_final = valor_produto - valor_desconto

# Visualização
print(f'O valor final é {valor_final:.2f}')
