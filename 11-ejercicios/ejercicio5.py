# Tabla dentro de un diccionario

tabla = [
    {
        "category": "PLATFORMS",
        "games": ["Celeste", "Shovel Knight", "Mario 3D World"]

    },
    {
        "category": "Beat'em UP",
        "games": ['Yakuza Kiwami 2', 'Scott Pilgrim VS The World: The Game']
    }
]
for category in tabla:
    print(category['category'])
    for game in category['games']:
        print(game)