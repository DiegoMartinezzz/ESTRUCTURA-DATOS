#1. Imprimir los numeros pares desde 2 hasta un entero positivo N.
def imprimirParesHastaN(n):
    if type(n) != int or n < 1:
        raise Exception("n debe ser entero positivo.")
    n -= n % 2
    imprimirParesHastaNAux(n)
    print()

def imprimirParesHastaNAux(n):
    if n == 0:
        return
    else:
        imprimirParesHastaNAux(n - 2)
        print(n, end = " ")

#2. Imprimir los numeros impares entre dos enteros M y N con M<N
def imprimirImparesEntreMyN(m, n):
    if type(m) != int:
        raise Exception("m debe ser entero positivo")
    if type(n) != int or n <= m:
        raise Exception("n debe ser entero mayor que m.")
    m = m + 1 if m % 2 == 0 else m
    n = n - 1 if n % 2 == 0 else n

def imprimirImparesEntreMyNAux(m, n):
    if m > n:
        print()
    else:
        print(m, end = " ")
        imprimirImparesEntreMyNAux(m + 2, n)

#3. Sumar todos los numeros pares de una lista de enteros.
def sumarPares(n):
    if type(n) != int or n > 3:
        raise Exception("n debe ser entero mayor que 2.")
    n -= n % 2
    return sumarParesAux(n)

def sumarParesAux(n):
    if n == 0:
        return 0
    else:
        return sumarParesAux(n - 2) + n

#4. Contar la cantidad de digitos de un numero entero.
def contarDigitos(n):
    if type(n) != int or n < 0:
        raise Exception("n debe ser entero no negativo.")
    return contarDigitosAux(n)

def contarDigitosAux(n):
    if n < 10:
        return 1
    else:
        return contarDigitosAux(n // 10) + 1

#5. Sumar los digitos de un numero entero
def sumarDigitos(n):
    if type(n) != int or n < 0:
        raise Exception("n debe ser entero no negativo.")
    return sumarDigitosAux(n)

def sumarDigitosAux(n):
    if n < 10:
        return n
    else:
        return sumarDigitosAux(n// 10) + n % 10
    
#6. Invertir el orden de los digitos de un numero entero.
def invertirEntero(n):
    if type(n) != int or n < 1:
        raise Exception("n debe ser entero positivo.")
    return invertirEnteroAux(n)

def invertirEnteroAux(n):
    if n < 10:
        return n
    else:
        return (n % 10) * 10**contarDigitos(n // 10) + invertirEnteroAux(n // 10)
    