import random

PS_jugador=       100
PS_oponente=      100
defensa_oponente= 100
defensa_jugador=  100

ataque ={
    "malicioso":                        (0,10), 
    "ascuas":                           (30,0), 
    "placaje":                          (35,0),
   } 
oponente={
    "1":                               (10,10),
    "2":                               (35,0 ),                       
    "3":                                (0,10)
   } 


 
while PS_jugador>0 and PS_oponente >0:
    print(f"""          
tu vida: {PS_jugador}
vida de oponente: {PS_oponente}""")
    print("="*50)
    
    ataque_jugador= input("elige tu ataque: ")
    ataque_jugador=ataque_jugador.lower()
    
    if ataque_jugador in ataque:
        
        if ataque_jugador=="placaje":
         a= ataque[ataque_jugador]
         tupla=(a[0]*(100/defensa_oponente), a[1])
        else: 
         tupla = ataque[ataque_jugador]
    else:
        print("<>"*35)
        print(
            "tus ataques son: malicioso, ascuas, placaje")
        continue
         
         
    
    PS_oponente-=        tupla[0]
    defensa_oponente-=   tupla[1]
    if defensa_jugador <= 0 :
         defensa_jugador=1
        
    ataque_oponente=str(random.randrange(1,3+1))
    
    if ataque_oponente == "2":
        b=      (oponente[ataque_oponente])
        tupla2=  (b[0]*(100/defensa_oponente),b[1])  #operación para defenir el daño en base a la defensa
    else:
     tupla2= (oponente[ataque_oponente])
     
    PS_jugador-=         tupla2[0]
    defensa_jugador-=    tupla2[1]
    if defensa_jugador <= 0 :
      defensa_jugador=1
if PS_oponente<= 0 and PS_jugador<=0:
        print("Empate")
elif PS_oponente <=0:
        print(" Felicidades, has ganado")
else:
        print(" lo siento, has perdido")

