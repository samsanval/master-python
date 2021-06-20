# Lista con ocho numeros enteros
# Recorrer y mostrarla
# Ordenarla y mostrarla
# Mostrar su longitud
# Buscar el elemento que pida por teclado

numbers = [1, 5, 3, 8, 6, 5, 4, 9]
for number in numbers:
    print(f"Numero {numbers.index(number)}: {number}")
numbers.sort()
for number in numbers:
    print(f"Numero {numbers.index(number)}: {number}")
print(f"Longitud de la lista {len(numbers)}")

numeroUsuario = int(input("Introduzca el numero a buscar: "))
if numeroUsuario in numbers:
    print(f"El numero está en la posición {numbers.index(numeroUsuario)+1}")
else:
    print('No está el número introducido')
