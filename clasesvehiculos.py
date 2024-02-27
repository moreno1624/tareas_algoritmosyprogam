x={}
aaa=["1","2","3","4","5"]
CARROS=1
BARCOS=2
AVIONES=3
REGISTROS=4
SALIR=5

class Seller:
    def __init__( self, nombre):
        self.nombre=nombre
    
    def __str__(self):
        return f"concesionario:{self.nombre}"
    
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
{REGISTROS})registros
{SALIR})salir        """)

     
def main():
    while True:
     print("="*35)
     menu()
     print("="*35)
     Y= input("elija numero para continuar: ")
     if Y in aaa:
         
         Y=int(Y)
     else:
         print("ingrese un valor válido")
         continue  
     
     if Y <4:
     
      registro=input("como quiere nombrar el registro(no repetir): ")
      print("="*35)
      seller=input("como se llama el concesionario: ")
      carac_1=input("cual es la marca de su vehiculo:  ")
      carac_2= input("cual es el modelo de su vehiculo:  ")
      
      if Y==CARROS :
          carros_input(registro,carac_1,carac_2)
          concesionario(seller,registro)
          continue
      elif Y==BARCOS:
          barcos_input(registro,carac_1,carac_2)
          concesionario(seller,registro)
          continue
      elif Y==AVIONES:
          avion_input(registro,carac_1,carac_2)
          concesionario(seller,registro)
          continue
     elif Y==REGISTROS:
          registro_input()
     elif Y==SALIR :
         break
     else:
         print("ingrese un valor válido")
         continue
     


def carros_input(registro,carac_1,carac_2):
    
 texto= " el color"
 carac_3= input(f"cual es {texto} de su vehiculo:  ")
 print("="*35)
 carrito=car(carac_1,carac_2,carac_3)
 x[registro]=[f"marca: {carrito.marca},modelo: {carrito.modelo},color: {carrito.color}"]
 return print(carrito)
 
def barcos_input(registro,carac_1,carac_2):
    
 texto=" el tipo"
 carac_3= input(f"cual es {texto} de su vehiculo:  ")
 print("="*35)
 carrito=barco(carac_1,carac_2,carac_3)
 x[registro]=[f"marca: {carrito.marca},modelo: {carrito.modelo},tipo: {carrito.tipo}"]
 return print(carrito)

def avion_input(registro,carac_1,carac_2):

 texto=" la capacidad"
 carac_3= input(f"cual es {texto} de su vehiculo:  ")
 print("="*35)
 carrito=avion(carac_1,carac_2,carac_3)
 x[registro]=[f"marca: {carrito.marca},modelo: {carrito.modelo},capacidad: {carrito.capacidad}"]
 return print(carrito)

def registro_input():
    if len(x)>0:
     registro=input("como se llama el registro buscado: ")
     print("="*35)
     if registro in x:
         print(f"{registro}= {x[registro]}")
     else:
         print("no se encontró el registro")
    else:
        print("no ha hecho ningun registro")
def concesionario(seller,registro):
    concesionario_=Seller(seller)
    x[registro]+=[f"concesionario : {concesionario_.nombre}"]
    return print(concesionario_)
    
main()