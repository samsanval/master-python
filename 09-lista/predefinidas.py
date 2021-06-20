cantantes = ['Yo', 'Bad bunny', 'Samuel']
numeros = [1, 45, 6, 12, 5]

numeros.sort()
print(numeros)
cantantes.append('Gaahl')
cantantes.insert(3,'David')
print(cantantes)

cantantes.pop(1)
cantantes.remove('Gaahl')
print(cantantes)

numeros.reverse()
print('Samuel' in cantantes)

print(len(numeros))
numeros.append(1)
print(numeros.count(1))