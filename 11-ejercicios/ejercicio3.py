# Comprueba si una variable está vacía y si lo está rellenarla con texto en minusculas y mostrarlo en mayúsculas

texto = ""
if len(texto.strip()) == 0:
    texto = "Esto es un texto".lower()
    print(texto.upper())
