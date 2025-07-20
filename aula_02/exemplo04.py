nomes = ['Messi', 'Eduardo', 'Mariaugusta', 'Agda']

print(nomes)

print(type(nomes))

print(nomes[0])
print(nomes[2])

nomes[2] = 'Julyana'
print(nomes)
nomes.insert(2, 'Mariaugusta')
print(nomes)
nomes.insert(100, 'Panda')
print(nomes)
del nomes[3]
print(nomes)

indice = nomes.index('Panda')
print(indice)

nome = input('Digite o nome: ')
indice = nomes.index(nome)
del nomes[indice]
print(nomes)
nomes.remove('Eduardo')
print(nomes)

indice = nomes.index('Agda')
nome_pop = nomes.pop(indice)
print(nomes)
print(nome_pop)

