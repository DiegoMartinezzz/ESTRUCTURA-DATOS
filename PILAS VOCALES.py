class Pila:
    def __init__(self):
        self.caja = []

    def meter(self,dato):
        self.caja.append(dato)

    def sacar(self):
        if len(self.caja) > 0:
            return self.caja.pop()
        else:
            return None
        
    def mostrar(self):
        return self.caja
        
    palabra = input("escribe una palabra:")
    pilaVocales = Pila()
    pilaConsonantes = Pila()

    for letra in palabra:
        if letra.lower() in "aeiou":
            pilaVocales.meter(letra)
        else:
            pilaConsonantes.meter(letra)

    print ("Pila de Vocales:", pilaVocales.mostrar())
    print ("Pila de Consonantes:", pilaConsonantes.mostrar())