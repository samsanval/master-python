name = input('Insert your name: ')
try:
    if len(name) > 1:
        username = "The user is " + name
    print(username)
except:
    print("There's been a mistake")
else:
    print("Everything is okay")
finally:
    print('End')
# Multiple exceptions
try:
    number = int(input("Tell me a number: "))
    print(f"{number * number}")
except TypeError:
    print('You must convert the string to int')
except ValueError:
    print('You shall pass a number')

# Raise Exception
try:
    name = input('Insert your name: ')
    age = int(input("Tell me a number: "))
    if age < 5 or age > 110:
        raise ValueError('The age is not real')
    elif len(name) <= 1:
        raise ValueError('The name is wrong')
    else:
        print(f"Bienvenido {name}")
except ValueError:
    print('Wrong')





