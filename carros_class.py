CARROS="1"
BARCOS="2"
AVIONES="3"
SALIR="4"
CCC=1
carros_list={}
barcos_list=[]
aviones_list=[]

def menu():
   print( f"""{CARROS})carros
{BARCOS})barcos
{AVIONES})aviones 
{SALIR}) salir        """)
def opcion1(carros_list):
    
 nombre=input("como quiere nombrar el registro: ")
 marca=input("cual es la marca de su carro:  ")
 modelo= input("cual es el modelo de su carro:  ")
 X=carros(marca,modelo)
 print(f"la marca es {X.marca} y el modelo {X.modelo}" )

 
        
def opcion2():
 X=input("como quiere nombrar el registro: ")
 capacidad=input("cual es la capacidad de personas de su barco:  ")
 longitud= input("cual es la longitud de su barco:  ")
 X=barcos(capacidad,longitud)
 print(f"la capacidad es {X.capacidad} y la longitud {X.longitud}" )
    
def opcion3():
 X=input("como quiere nombrar el registro: ")
 tipo=input("cual es el tipo  de su avion:  ")
 modelo= input("cual es el modelo de su avion:  ")
 X=avion(tipo,modelo)
 print(f"el tipo es{X.tipo} y el modelo {X.modelo}" )
          
class carros:
    def __init__(self, marca, modelo):
        self.marca= marca
        self.modelo= modelo
        print("carro")
class barcos:
    def __init__(self, capacidad, longitud):
        self.capacidad= capacidad
        self.longitud= longitud
        print("barco")
class avion:
    def __init__(self,tipo, modelo ):
        self.tipo= tipo
        self.modelo= modelo
        print("avion")
        
def main():
    while True:
     print("="*35)
     menu()
     print("="*35)
     Y= input("que vehículo quiere registrar: ")
     if Y==CARROS :
         opcion1(carros_list)
         continue
     elif Y==BARCOS:
         opcion2()
         continue
     elif Y==AVIONES:
         opcion3()
         continue
     elif Y==SALIR :
         break
     else:
         print("ingrese un valor válido")
         continue
main()
        
        
