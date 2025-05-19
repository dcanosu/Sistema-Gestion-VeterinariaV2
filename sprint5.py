from datetime import datetime
import logging
logging.basicConfig(filename="clinica_veterinaria.log", format='%(asctime)s - %(levelname)s - %(message)s',level=logging.INFO)

class Titulos:
    @staticmethod
    def imprimir_titulo(texto):
        print("\n" + "=" * 60)
        print(f"{texto.center(60)}")
        print("=" * 60 + "\n")
        
class Mensajes:
    @staticmethod
    def imprimir_mensaje(texto):
        print("\n * " + texto)

class Mascota:
    """
    Representa una mascota registrada en la veterinaria.

    Atributos:
        nombre (str): Nombre de la mascota.
        especie (str): Especie de la mascota (perro, gato, etc.).
        raza (str): Raza de la mascota.
        edad (int): Edad de la mascota en años.
        dueno (Dueno): Objeto que representa al dueño de la mascota.
    """
    def __init__(self, nombre, especie, raza, edad, propietario):  #Se crea la clase, se usa el metodo constructor init para inicializarla
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.propietario = propietario
        
    def __str__(self):
        propietario_nombre = self.propietario.nombre if self.propietario else "Sin propietario"
        return (     
            f"Nombre: {self.nombre}\n"
            f"Especie: {self.especie}\n"
            f"Raza: {self.raza}\n"
            f"Edad: {self.edad}\n"
            f"Propietario: {propietario_nombre}"
        )
    
class Propietario:
    """
    Representa al dueño de una mascota.

    Atributos:
        nombre (str): Nombre del dueño.
        telefono (str): Teléfono de contacto.
        direccion (str): Dirección de residencia.
    """
    def __init__(self, nombre, telefono, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion      

    def __str__(self):
        return (
            f"Nombre: {self.nombre}\n"
            f"Telefono: {self.telefono}\n"
            f"Direccion: {self.direccion}"
        )
    
class Consulta:
    """
    Registro de una consulta médica para una mascota.

    Atributos:
        fecha (str): Fecha de la consulta.
        motivo (str): Motivo de la visita.
        diagnostico (str): Diagnóstico emitido.
        mascota (Mascota): Mascota asociada a la consulta.
    """
    def __init__(self, fecha, motivo, diagnostico, mascota):
        self.fecha = fecha
        self.motivo = motivo
        self.diagnostico = diagnostico
        self.mascota = mascota  #Se usa para llamar la clase Mascota
        
    def __str__(self):
        return (
            f"Fecha: {self.fecha}\n"
            f"Motivo: {self.motivo}\n"
            f"Diagnostico: {self.diagnostico}\n"
            f"Mascota: {self.mascota.nombre}\n"
        )

class SistemaVeterinaria:
    """
    Sistema principal para gestionar el funcionamiento de la veterinaria:
    registro de mascotas, dueños y consultas.
    """
    def __init__(self):        
        self.mascotas= []
        self.propietarios= []
        self.consultas = []

    def registrar_propietario(self):
        """
        Solicita datos por consola y registra un nuevo dueño en el sistema.

        Retorna:
            Dueno: Objeto del dueño registrado.
        """
        Titulos.imprimir_titulo("Registrar propietario")
        nombre= input("Nombre del dueño: ").strip()
        telefono= input("Teléfono del dueño: ")
        direccion= input("Dirección del dueño: ")
        propietario = Propietario(nombre, telefono, direccion)
        self.propietarios.append(propietario)
        print("Dueño registrado")
        logging.info(f"Se registró al dueño: {nombre}")
        return propietario

    def buscar_propietario(self, nombre_propietario): #para saber si el dueño ya esta inscrito se hace una verificación "nombre_propietario" va a ser pedido cuando el usuario registre su mascota
        """
        Busca un dueño registrado por nombre (ignorando mayúsculas/minúsculas).

        Parámetros:
            nombre_propietario (str): Nombre del dueño a buscar.

        Retorna:
            Dueno o None: Objeto del dueño si existe, de lo contrario None.
        """
        for propietario in self.propietarios:
            if propietario.nombre.lower()==nombre_propietario.lower():  #para evitar dolores de cabeza, se le pide que no discrimine por mayuscula
                return propietario
        return None

    def registrar_mascota(self):
        """
        Registra una nueva mascota. Si el dueño no está registrado, lo solicita.
        """
        Titulos.imprimir_titulo("Registro de mascota")
        nombre=input("Nombre de la mascota: ")
        especie=input("Especie de la mascota: ")
        raza=input("Raza de la mascota: ")
        
        while True:
            try:
                edad = int(input("Edad de la mascota en años: "))
                break
            except ValueError:
                logging.error("Error al ingresar la edad de la mascota, se ingresó un valor no valido")
                print("Por favor, ingrese un número válido.")

        nombre_propietario = input("Nombre del dueño: ").strip() #Esto buscará si el dueño ya esta registrado, de otra forma, pedira que lo registre
        propietario=self.buscar_propietario(nombre_propietario)
        
        if not propietario:
            Mensajes.imprimir_mensaje("El dueño no está registrado. Por favor, regístrelo.")
            propietario=self.registrar_propietario()
        
        mascota= Mascota(nombre, especie, raza, edad, propietario)
        self.mascotas.append(mascota)
        print(f"\n - Mascota '{mascota.nombre}' registrada.")
        logging.info(f"Se registró la mascota: {mascota.nombre}, del dueño: {propietario.nombre}")

    def listar_mascotas(self):
        """
        Muestra por consola todas las mascotas registradas en el sistema.
        """
        
        Titulos.imprimir_titulo("Lista de mascotas")
        if not self.mascotas:
            Mensajes.imprimir_mensaje("No existen mascotas registradas")
            logging.info("Se intento consultar la lista de mascotas, pero no hay registros")
            return

        for mascota in self.mascotas:
            print(mascota)
            print("-" * 30)         
        logging.info("Se consultaron las mascotas registradas")

    def registrar_consulta(self):
        """
        Registra una consulta médica para una mascota existente.
        """
        Titulos.imprimir_titulo("Registro de Consulta")
        nombre_mascota = input("Nombre de la mascota: ")

        mascota = next((m for m in self.mascotas if m.nombre.lower() == nombre_mascota.lower()), None)
        if not mascota:
            Mensajes.imprimir_mensaje("Mascota no encontrada")
            logging.info("Se intentó registrar una consulta para una mascota no registrada")
            return

        while True:
            fecha_input = input("Fecha de la consulta (dd-mm-aaaa): ")
            try:
                fecha = datetime.strptime(fecha_input, "%d-%m-%Y").date()
                break
            except ValueError:
                logging.error("Error al ingresar la fecha de la consulta, se ingresó un valor no valido")
                print("Formato incorrecto o fecha inválida. Ejemplo válido: 15-03-2025.")
    
        motivo = input("Motivo de la consulta: ")
        diagnostico = input("Diagnóstico: ")

        consulta = Consulta(fecha, motivo, diagnostico, mascota)
        self.consultas.append(consulta)
        print("Consulta registrada.")
        logging.info(f"Se registró una consulta de la mascota: {mascota.nombre}")

    def historia_clinica(self):
        """
        Muestra el historial clínico (consultas) de una mascota específica.
        """
        Titulos.imprimir_titulo("Historia Clínica")
        nombre_mascota = input("Nombre de la mascota: ")

        consultas = [c for c in self.consultas if c.mascota.nombre.lower() == nombre_mascota.lower()]
        if not consultas:
            Mensajes.imprimir_mensaje("No hay consultas registradas para esta mascota.")
            logging.info(f"No se encontraron consultas para la mascota: {nombre_mascota}")
            return

        print(f"\nHistorial clínico de {nombre_mascota}:")
        for consulta in consultas:
            print(consulta)
        logging.info(f"Se consultó la historia clínica de la mascota: {nombre_mascota}")
        
def main():
    """
    Función principal que lanza el menú interactivo del sistema veterinario.
    """
    logging.info("Se inició la aplicación")
    sistema=SistemaVeterinaria() #Con esto nos aseguramos de usar la clase SistemaVet que tiene todas las funciones del codigo
    while True:
        Titulos.imprimir_titulo("Bienvenido al sistema de la veterinaria Amigos Peludos")
        
        print("1. Registrar mascota")
        print("2. Registrar consulta")
        print("3. Lista de mascotas")
        print("4. Historia clinica de mascota")
        print("5. Salir del sistema")
        
        Mensajes.imprimir_mensaje("¿En qué podemos ayudarlo? Elija un número: ")
        opcion = input("> ")
        
        if opcion == '1':
            sistema.registrar_mascota()
        elif opcion == '2':
            sistema.registrar_consulta()
        elif opcion == '3':
            sistema.listar_mascotas()
        elif opcion == '4':
            sistema.historia_clinica()
        elif opcion == '5':
            print("¡Gracias por usar el sistema! Hasta luego.")
            logging.info("Se cerró la aplicación")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__=="__main__":
    main()