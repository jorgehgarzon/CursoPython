
import json

variable_string = '{"nombre": "Andres", "apellidos":"Perez"}'
print(type(variable_string))
print(variable_string)
variable_python = json.loads(variable_string)
print(type(variable_python))
print(variable_python)

lista = [("texto", 1, 6.7), ({"nombre": "Andres", "apellidos":"Perez"})]
variable_json = json.dumps(lista)
print(type(lista))
variable_json = lista
print(type(variable_python))
print(variable_python)
