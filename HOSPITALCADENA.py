# Clase Cliente
class Cliente:
    def __init__(self, nombre, transaccion):
        self.nombre = nombre
        self.transaccion = transaccion

    def __str__(self):
        return f"{self.nombre} - {self.transaccion}"

# Clase Cola
class Cola:
    def __init__(self):
        self.items = []

    def enqueue(self, dato):
        self.items.append(dato)

    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

    def mostrar(self):
        if self.is_empty():
            print("No hay clientes en la fila.")
        else:
            print("Clientes en espera:")
            for i, cliente in enumerate(self.items, start=1):
                print(f"{i}. {cliente}")


# Programa principal
cola_hospital = Cola()

while True:
    print("\n=== Hospital ===")
    print("1. Agregar a un paciente")
    print("2. Atender a pasiente")
    print("3. Ver pacientes en espera")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre del cliente: ")
        # Validar transacción
        transaccion = ""
        while transaccion not in ["inversion", "cuenta", "normal"]:
            transaccion = input("Tipo de transacción (inversion/cuenta/normal): ").lower()
        cola_hospital.enqueue(Cliente(nombre, transaccion))
        print(f"Cliente {nombre} agregado a la fila.")

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