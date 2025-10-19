class Pilas:
    def __init__(self):
        self.consonantes=[]
        self.vocales=[]
        self.numeros=[]
        self.cadena1=""
    def Cadena(self):
        self.cadena1=input("Ingresa la cadena: ").lower()
    def proceso(self):
        for j in self.cadena1:
            if j in "aeiou":
                self.vocales.append(j)
            elif j in "1234567890":
                self.numeros.append(j)
            elif j.isalpha():
                self.consonantes.append(j)
    
    def resultado (self):
        print("Las consonantes de la cadena son: ",self.consonantes)
        print("Las vocales de la cadena son: ",self.vocales)
        print("los numeros de la cadena son: ",self.numeros)
obj= Pilas()
obj.Cadena()
obj.proceso()
obj.resultado()