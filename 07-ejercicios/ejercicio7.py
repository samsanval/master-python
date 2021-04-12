numero1 = int(input('Introduzca el primer numero '))
numero2 = int(input('Introduzca el segundo numero '))

for i in range(numero1, numero2):
    if i % 2 != 0:
        print(i)
