#### \\\\ EJERCICIO 2 - Insertar despues de un valor ////####

#Enunciado: Crea insert_after(valor_objetivo, x) 
#que inserte un nodo con x después de la primera
#ocurrencia de valor_objetivo. Si no existe, no inserta.

def find(self, v):
    cur = self.head
    while cur:
        if cur.dato == v: return cur
        cur = cur.next
    return None

def insert_after(self, objetivo, x):
    nodo = self.find(objetivo)
    if not nodo: return
    n = nodo(x)
    n.prev = nodo
    n.next = nodo.next
    if nodo.next: nodo.next.prev = n
    else: self.tail = n
    nodo.next = n

#Prueba rápida: con [5,10,20,30], insert_after(10, 15) → [5,10,15,20,30].
#Complejidad: búsqueda O(n), enlace O(1).