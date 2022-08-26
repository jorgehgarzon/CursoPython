import json

json_object =  '''{
    "nombre": "Eduardo",
    "edad": 27,
    "correo": "eduardo78d@gmail.com",
    "cursos": ["Python", "MongoDB", "Flask"]
}'''

user = json.loads(json_object)
print(user)