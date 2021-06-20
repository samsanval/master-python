pelicula = "Scott Pilgrim"
# List
peliculas = [pelicula, "500 days of summer", "Eternal spotless of mind"]
cantantes = list(('Bruce Dickinson', 'Rob Halford', 'Ronnie James Dio'))
years = list(range(0, 10))
listMultiple = ["Samuel",10,True]

# Indices
print(peliculas[0])
print(peliculas[-1])
print(cantantes[1:3])
print(cantantes[2:])

cantantes.append('Peter Tangtren')
print(cantantes)

# FOR
for film in peliculas:
    print(f"{peliculas.index(film)}. {film}")

# Multiarray
contacts = [
    [
        'Antonio', 'antonio@com'
    ],
    [
        'Pep', 'pep@com'
    ],
    [
        'Salvador', 'salva@com'
    ]
]
print(contacts)
for contact in contacts:
    for elem in contact:
        print(elem)

# Metodos


