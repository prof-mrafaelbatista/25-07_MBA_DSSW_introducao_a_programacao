import time
lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# len = Calcula o tamanho do objeto
tam_vet = len(lista) #3

for num in range(tam_vet): #range(3) 0, 1, 2
    print(f'For externo: {lista[num]}')
    time.sleep(2)

    for num2 in range(len(lista[num])): #3
        print(f'For interno: lista[{num}][{num2}] - {lista[num][num2]}')
        time.sleep(2)

