# Clase Cliente
class Cliente:
    def __init__(self, nombre, transaccion):
        self.nombre = nombre
        self.transaccion = transaccion

    def __str__(self):
        return f"{self.nombre} - {self.transaccion}"


# Clase Cola con prioridad
class Cola:
    def __init__(self):               #se quito la lista 
        self.inversion = []           # se agregaron las 3
        self.cuenta = []
        self.normal = []

    def enqueue(self, cliente):                   
        if cliente.transaccion == "inversion":   #los agregan a las cola
            self.inversion.append(cliente)
        elif cliente.transaccion == "cuenta":
            self.cuenta.append(cliente)
        else:
            self.normal.append(cliente)

    def dequeue(self):
        if self.inversion:
            return self.inversion.pop(0)
        elif self.cuenta:
            return self.cuenta.pop(0)
        elif self.normal:
            return self.normal.pop(0)
        else:
            return None

    def is_empty(self):           #revisa listas
        return not (self.inversion or self.cuenta or self.normal)

    def mostrar(self):       #se imprimen las 3 listas
        if self.is_empty():
            print("No hay clientes en la fila.")
        else:
            print("\nClientes en espera (por prioridad):")
            print("\n--- Inversión ---")
            for i, cliente in enumerate(self.inversion, start=1):
                print(f"{i}. {cliente}")
            print("\n--- Cuenta ---")
            for i, cliente in enumerate(self.cuenta, start=1):
                print(f"{i}. {cliente}")
            print("\n--- Normal ---")
            for i, cliente in enumerate(self.normal, start=1):
                print(f"{i}. {cliente}")


# Programa principal
cola_hospital = Cola()

while True:
    print("\n=== Hospital ===")
    print("1. Agregar a un paciente")
    print("2. Atender a paciente")
    print("3. Ver pacientes en espera")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre del cliente: ")
        transaccion = ""
        while transaccion not in ["inversion", "cuenta", "normal"]:
            transaccion = input("Tipo de transacción (inversion/cuenta/normal): ").lower()
        cola_hospital.enqueue(Cliente(nombre, transaccion))
        print(f"Cliente {nombre} agregado a la fila con transacción '{transaccion}'.")

    elif opcion == "2":
        cliente = cola_hospital.dequeue()
        if cliente:
            print(f"Atendiendo a {cliente}")
        else:
            print("No hay clientes para atender.")

    elif opcion == "3":
        cola_hospital.mostrar()

    elif opcion == "4":
        print("Saliendo del sistema. ¡Gracias!")
        break

    else:
        print("Opción inválida, intenta de nuevo.")