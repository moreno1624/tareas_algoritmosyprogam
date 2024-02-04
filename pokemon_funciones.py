import random
jugador=[100,100]
oponente=[100,100]


def placaje(oponente) :
    x=35 *(100/oponente[1])
    return oponente[0]-x 

def ascuas(oponente) :
    x=30
    return oponente[0]-x

def malicioso(oponente) :
    x=10
    return oponente[1]-10

def latigo(jugador):
    x=10
    return [jugador[0]-10 , jugador[1]-10]

def placaje(jugador) :
    x=35 *(100/jugador[1])
    return jugador[0]-x
def malicioso(jugador) :
    x=10
    return jugador[1]-10

while jugador[0]>0 and oponente[0]>0:
    print(f"""          
tu vida: {jugador[0]}
tu defensa: {jugador[1]}
vida de oponente: {oponente[0]}
defensa oponente {oponente[1]}
""")
    print("="*50)
    
    ataque= input("elige tu ataque: ")
    ataque=ataque.lower()
    
   
        
    if ataque=="placaje":
         print("usaste",ataque)
         oponente[0]=placaje(oponente)
    elif ataque=="ascuas":
         print("usaste",ataque)
         oponente[0]=ascuas(oponente)
    elif ataque=="malicioso":
      oponente[1]=malicioso(oponente)
      print("usaste",ataque)
    else:
         print("<>"*35)
         print(
            "tus ataques son: malicioso, ascuas, placaje")
         continue   
    if oponente[1]<= 0 :
         oponente[1]=1
        
    ataque_oponente=random.randrange(1,3+1)
    
    if ataque_oponente == 1:
     jugador[0]=latigo(jugador)[0]
     jugador[1]=latigo(jugador)[0]
    elif ataque_oponente == 2:
     jugador[0]=placaje(jugador)
    elif ataque_oponente == 3:
     jugador[1]=malicioso(jugador) 
    if jugador[1] <= 0 :
      jugador[1]=1
if jugador[0]<= 0 and oponente[0]<=0:
        print("Empate")
elif oponente[0] <=0:
        print(" Felicidades, has ganado")
else:
        print(" lo siento, has perdido")
print("nos vemos...")
