# import myModule
from myModule import *
from datetime import *
from math import *
from random import randint

print(helloworld('Samuel'))

# Datetime
print(date.today())
dateComplete = datetime.now()
print(dateComplete)
print(dateComplete.year)
print(dateComplete.strftime("%d/%m/%Y, %H:%M"))
print(datetime.now().timestamp())

# Math
print(f"Raiz cuadrada de 25 {sqrt(25)}")
print(pi)
print(ceil(pi))
print(floor(pi))
print(randint(15, 67))

