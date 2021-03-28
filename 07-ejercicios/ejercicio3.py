#Imprimir los cuadrados de los 60 primeros numeros naturales con while y for

i = 0
while i < 60:
    print(f"Con el bucle while {i*i}")
    i = i+1
for i in range(0, 60):
    print(f"Con el bucle for {i*i}")
