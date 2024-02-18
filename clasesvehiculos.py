CARROS="1"
BARCOS="2"
AVIONES="3"
SALIR="4"

class Vehiculos:
    def __init__(self, marca, modelo):
        self.marca= marca
        self.modelo= modelo
    def __str__(self):
        return f"marca: {self.marca},modelo: {self.modelo}"
class car(Vehiculos):
    def __init__(self, marca, modelo, color):
        Vehiculos.__init__(self, marca, modelo)
        self.color=color
    def __str__(self):
        return f"marca: {self.marca}, modelo: {self.modelo}, color: {self.color}"
    
class barco(Vehiculos):
    def __init__(self, marca, modelo, tipo):
        Vehiculos.__init__(self, marca, modelo)
        self.tipo=tipo
    def __str__(self):
        return f"marca: {self.marca}, modelo: {self.modelo}, tipo: {self.tipo}"

class avion(Vehiculos):
    def __init__(self, marca, modelo,capacidad):
        Vehiculos.__init__(self, marca, modelo)
        self.capacidad=capacidad
    def __str__(self):
        return f"marca: {self.marca}, modelo: {self.modelo}, capacidad: {self.capacidad}"
    

def menu():
 print( f"""{CARROS})carros
{BARCOS})barcos
{AVIONES})aviones 
{SALIR}) salir        """)


     
def main():
    while True:
     print("="*35)
     menu()
     print("="*35)
     Y= input("que vehículo quiere registrar: ")
     if Y==CARROS :
      Input(Y)
      continue
     elif Y==BARCOS:
         Input(Y)
         continue
     elif Y==AVIONES:
         Input(Y)
         continue
     elif Y==SALIR :
         break
     else:
         print("ingrese un valor válido")
         continue
     
def Input(Y):
 registro=input("como quiere nombrar el registro: ")
 carac_1=input(f"cual es la marca de su vehiculo:  ")
 carac_2= input(f"cual es el modelo de su vehiculo:  ")
 if Y=="1":
     texto= " el color"
     carac_3= input(f"cual es {texto} de su vehiculo:  ")
     registro=car(carac_1,carac_2,carac_3)
     return print(registro)
 elif Y=="2":
     texto=" el tipo"
     carac_3= input(f"cual es {texto} de su vehiculo:  ")
     registro=barco(carac_1,carac_2,carac_3)
     return print(registro)
 elif Y=="3":   
     texto=" la capacidad"
     carac_3= input(f"cual es {texto} de su vehiculo:  ")
     registro=avion(carac_1,carac_2,carac_3)
     return print(registro)
 
 
main()
