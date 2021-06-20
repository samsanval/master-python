# Añadir valores a una lista mientras su longitd sea menor de 120

def addUntil120():
    list = []
    i = 0
    while len(list) < 120:
        list.append(i)
        i = i + 1
    print(list)


addUntil120()
