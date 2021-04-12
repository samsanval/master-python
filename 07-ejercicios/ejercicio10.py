# Pedir la nota de 15 alumnos y ver cuantos han aprobado y cuantos han
numero = 0
for i in range(0, 15):
    nota = int(input(f'Introduzca la nota del numero {i} '))
    if nota >= 5:
        numero = numero + 1
print(f"Han aprobado {numero} alumnos")
