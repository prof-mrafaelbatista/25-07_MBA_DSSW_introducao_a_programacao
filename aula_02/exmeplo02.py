idade = int(input("Digite a sua idade: "))
ingresso = input("Ingresso VIP ou PISTA: ").upper()

print(f'O ingresso foi {ingresso}.')

if idade >= 18 and ingresso == "VIP":
    print("Siga para o primeiro andar.")
else:
    print("É hora de voltar para sua casa")
