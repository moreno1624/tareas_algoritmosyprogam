import random

PS_jugador= 100
PS_oponente= 100
defensa_oponente=100
defensa_jugador= 100
ataques = ["malicioso", "ascuas", "placaje"]
while PS_jugador>0 and PS_oponente >0:
    print("tu vida:", PS_jugador, "vida de oponente:" ,PS_oponente)
    ataque_jugador= input("ataque: ")
    ataque_jugador=ataque_jugador.lower()
    if ataque_jugador == ataques[0]:
        defensa_oponente = defensa_oponente -10
        if defensa_oponente <= 0 :
            defensa_oponente=1
    elif ataque_jugador == ataques[2]:
        PS_oponente-=35* (100/defensa_oponente)
    elif ataque_jugador ==ataques[1]:
        PS_oponente-=30
    else:
        print(" Que estas haciendo, tus ataques son malicioso,ascuas,placaje")
        continue
    
    ataque_oponente=random.randrange(1,3+1)
    if ataque_oponente == 1:
        defensa_jugador= defensa_jugador -10
        if defensa_jugador <= 0 :
            defensa_jugador=1
    elif ataque_oponente==2:
        PS_jugador-=35* (100/defensa_jugador)
    elif ataque_oponente== 3 :
        PS_jugador-= 40

if PS_oponente<= 0 and PS_jugador<=0:
        print("Empate")
elif PS_oponente <=0:
        print(" Felicidades, has ganado")
else:
        print(" lo siento, has perdido")