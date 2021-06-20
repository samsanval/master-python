persona = {
    "nombre": "samuel",
    "apellidos": "sanchez"
}
print(persona)
print(type(persona))
print(persona["nombre"])

contactos = [
    {
        'nombre': 'Samuel',
        'email': 'samuel@com'
    },
    {
        'nombre': 'Luis',
        'email': 'luis@com'
    },
    {
        'nombre': 'Juan',
        'email': 'juan@com'
    }
]
print(contactos[0]['email'])
for contacto in contactos:
    print(f"Nombre del contacto {contacto['nombre']}")
