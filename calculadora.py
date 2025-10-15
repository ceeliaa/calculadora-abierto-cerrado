
# URL github: https://github.com/ceeliaa/calculadora-abierto-cerrado.git 


from abc import ABC, abstractmethod

# Clase padre de la que van a heredar las demás. Todos van a seguir el modo de operar
class Operacion(ABC):
    @abstractmethod
    def ejecutar(self, a, b):
        pass

# Siguiendo el princpio de responsabilidad única, creo 4 clases independientes que cada una hace una única operación. Si tuviese que añadir
# otra clase, añadiría otra clase aqui sin tocar las demás
class Suma(Operacion):
    def ejecutar(self, a, b):
        return a + b
    
class Resta(Operacion):
    def ejecutar(self, a, b):
        return a - b


class Multiplicacion(Operacion):
    def ejecutar(self, a, b):
        return a * b


class Division(Operacion):
    def ejecutar(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir entre cero.")
        return a / b

class Potencia(Operacion):
    def ejecutar(self, a, b):
        return a ** b
    

# Siguiendo el principio abierto / cerrado (abierta para su extensión, cerrada para su modificación)
# No hace falta cambiar ninguna línea de calculadora para agregar una nueva operación
# En esta clase si necesito un constructor (init) porque me importa el estado, empiezo creando un diccionario vacío
# self.operaciones donde se guardan las operaciones que se registran. El resto no guardan atributos, solo definen qué hace la operación.
class Calculadora:
    def __init__(self):
        self.operaciones = {}

    def registrar_operacion(self, nombre, operacion):
        self.operaciones[nombre] = operacion

    def calcular(self, nombre, a, b):
        if nombre not in self.operaciones:
            raise ValueError(f"Operación '{nombre}' no registrada.")
        operacion = self.operaciones[nombre]
        return operacion.ejecutar(a, b)
    

if __name__ == "__main__":
    calculadora = Calculadora()

    # Registrar operaciones (OCP → se pueden añadir nuevas sin tocar la clase Calculadora, por ej, si quiero meter potencia, meto aquí potencia y añado 
    # una clase, no tendría que tocar la clase Calculadora para nada)
    calculadora.registrar_operacion("sumar", Suma())
    calculadora.registrar_operacion("restar", Resta())
    calculadora.registrar_operacion("multiplicar", Multiplicacion())
    calculadora.registrar_operacion("dividir", Division())
    calculadora.registrar_operacion("potencia", Potencia())

    # Ejemplo de uso
    print("Suma:", calculadora.calcular("sumar", 10, 5))
    print("Resta: ", calculadora.calcular("restar", 20, 5))
    print("Multiplicación: ", calculadora.calcular("multiplicar", 5,3))
    print("División:", calculadora.calcular("dividir", 30, 3))
    print("Potencia", calculadora.calcular("potencia", 2, 3))


