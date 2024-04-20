"""
=====================================
Ejemplo de Clases (POO) con Python
=====================================
"""
class Persona:

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def correr(self):
        return self.nombre + ' esta corriendo'
    def comer(self):
        return self.nombre + ' esta comiendo'

persona1 = Persona('Saul', 'Chavez', 25)
persona2 = Persona('Jose', 'Hernandez', 30)

print(persona1.nombre)
print(persona1.correr())
print(persona2.comer())


