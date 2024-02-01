import random

PS_jugador=       100
PS_oponente=      100
defensa_oponente= 100
defensa_jugador=  100

ataque ={
    "malicioso":                        (0,10), 
   "ascuas":                            (30,0), 
   "placaje":                           (35,0),
   } 
oponente={
    "1":                               (10,10),
    "2":                               (35,0 ),                       
    "3":                                (0,10)
   } 
print(" acuerdese que sus ataques son ascuas, malicioso, placaje, si se equivoca se acaba la partida automáticamente")

 
while PS_jugador>0 and PS_oponente >0:
    print("tu vida:", PS_jugador, "vida de oponente:" ,PS_oponente)
    ataque_jugador= input("ataque: ")
    ataque_jugador=ataque_jugador.lower()
    
    if ataque_jugador == "placaje":
     a= ataque[ataque_jugador]
     tupla=(a[0]*(100/defensa_oponente), a[1])
    elif ataque_jugador == "ascuas" or "malicioso": 
        tupla = ataque[ataque_jugador]
    else:
        pass
    
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
        

