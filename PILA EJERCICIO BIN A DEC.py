#CREA UN PROGRAMA QUE SE ENCARGUE DE TRANSFORMAR UN NUMERO BINARIO
#A DECIMAL SIN UTILIZAR FUNCIONES PROPIAS DEL LENGUAJE QUE
#LO HAGAN DIRECTAMENTE.

####determinar operaciones
#definir numero de numeros
#pila numero x 2 a la numero de dato-1
####determinar conjunto de datos
#ordenar todos los numeros en pila(el primero que llega es el ultimo en salir), determinar cuantos numeros hay,
#agarrar el primero y multiplicar por 2 a la 0, 
#agarrar el que sigue y multiplicar por 2  a la 1 y asi sucesivamente  hasta terminar con los numeros
####analisis a priori
####analisis a posteriori

class Pila:
  def __init__(self):               #crea una lista
    self.items=[]      

  def push(self,datos):             #agrega un elemento a la pila
    self.items.append(datos)    

  def pop(self):                    #saca al ultimo elemento en entrar
    return self.items.pop() if not self.is_empty() else None

  def is_empty(self):               #revisa si la pila essta vacia
    return len(self.items)==0
  
def binarioADecimal(binario):
    pila = Pila()

    for digito in binario:          #inserta cada numero binario en la pila
        pila.push(int(digito))

    decimal = 0
    exponente = 0

    while not pila.is_empty():          #mientras la pila no este vacia,
        bit = pila.pop()                  # agarrar el ultimo elemento
        decimal += bit * (2 ** exponente)   #multiplicar x2 a la exponente(que empieza en 0 y se va sumando 1) se ponen en "decimal" y se suman los resultados
        exponente += 1

    return decimal

binario = input("Ingresa un número binario: ")
decimal = binarioADecimal(binario)
print(decimal)