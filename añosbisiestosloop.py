x=1
N_añosb=0
Años_b=[]
año= int(input("escriba un año entre 1900 y 2199: "))
print("="*35)
if año>1900 and año<2199:
    for i in range(1900,año+1):
        if i%4==0 and i%100!=0 or  i%4==0 and i%100==0 and i%400==0:
            N_añosb+=1
            Años_b.append(i)
        else:
            pass
    print(f"numero de años bisiestos: {N_añosb} / años bisiestos: {Años_b}")
else:
    print("ingrese un valor valido")
    