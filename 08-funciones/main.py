def example():
    print('Ejecuto la funcion')


example()


def second_example(param):
    print(f"Escribo la funcion usando el param {param}")


second_example('Samuel')


def options(nombre, dni=None):
    print(f'{nombre}')
    print(f"{dni}")


options('Samuel', '212')


def helloworld(nombre):
    return f"Hello {nombre}"


print(helloworld('Samuel'))

# Lambda functions

year = lambda yearinput: f"El año es {yearinput}"

print(year(1991))
