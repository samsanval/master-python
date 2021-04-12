nombre = "Samuel"

print(type(nombre))

check = isinstance(nombre, str)
if check:
    print('Es string')
else:
    print('No')

blankstring = "               hola              "
print(blankstring.strip())

year = 2021
print(year)
del year

texto = " fff "
if len(texto) > 0:
    print(len(texto))

lavida = "El sentido de la vida"
print(lavida.find("sentido"))

nuevafrase = lavida.replace("vida", "brian")
print(nuevafrase)

print(nuevafrase.upper())
print(nuevafrase.lower())
