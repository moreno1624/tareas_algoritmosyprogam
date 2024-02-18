año= int(input("escriba un año entre 1900 y 2199: "))

if año<1900 and año>2199:
    print(" año no válido ")
    quit()
else:
    pass
if año%4==0 and año%100!=0 or  año%4==0 and año%100==0 and año%400==0:
    
    print("tu año es bisiesto")
else:
    print("tu año no es bisiesto")
    
añobisiesto= int((año-1900)//4-(año-1900)//100+(año-1900)//400)
    
print(añobisiesto)  

