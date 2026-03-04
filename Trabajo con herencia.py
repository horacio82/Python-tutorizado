#PILDORAS INFORMATICAS
#Python tutorizado. POO VIII, XI, X - Vídeos 36, 37, 38:

class Persona:
    def __init__(self, nombre, apellido, edad, *args, **kwargs):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def getDatosPersonales(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}"


class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, escuela, *args, **kwargs):
        super().__init__(nombre, apellido, edad, *args, **kwargs)
        self.escuela = escuela

    def getDatosPersonales(self):
        return f"{super().getDatosPersonales()}, Escuela: {self.escuela}"


class Trabajador(Persona):
    def __init__(self, nombre, apellido, edad, empresa, *args, **kwargs):
        super().__init__(nombre, apellido, edad, *args, **kwargs)
        self.empresa = empresa

    def getDatosPersonales(self):
        return f"{super().getDatosPersonales()}, Empresa: {self.empresa}"


class Director(Estudiante, Trabajador):
    def __init__(self, nombre, apellido, edad, empresa, escuela, bonus, *args, **kwargs):
        super().__init__(nombre, apellido, edad, escuela=escuela, empresa=empresa, *args, **kwargs)
        self.bonus = bonus

    def getDatosPersonales(self):
        return f"{super().getDatosPersonales()}, Bonus: {self.bonus}"


# --- PRUEBAS ---
persona1 = Persona("Ana", "Gómez", 35)
estudiante1 = Estudiante("Juan", "Diaz", 32, "San Javier")
trabajador1 = Trabajador("Antonio", "López", 55, "C Cope")
director1 = Director("Juan M", "Díaz", 21, "Píldoras Informáticas", "San Juan", 1500)

print("--- Persona y Estudiante ---")
print(persona1.getDatosPersonales())
print(estudiante1.getDatosPersonales())

print("\n--- Trabajador ---")
print(trabajador1.getDatosPersonales())

print("\n--- Director (Herencia Múltiple) ---")
print(director1.getDatosPersonales())