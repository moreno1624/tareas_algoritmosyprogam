nombre = float(input("cuantas arepas quieres hacer "))
a = nombre * 1/16
b = nombre * 1/3/16 
x= float(input("cuantas tazas de harina tienes"))
if x>= nombre:
    print("tienes la cantidad necesaria, usarás", nombre, "tazas de harina")
else:
    print("no tines la cantidad necesaria, compra más producto")
    quit()
    
y= float(input("cuantas tazas de agua tienes"))
if y>= nombre:
    print("tienes la cantidad necesaria, usarás", nombre, "tazas de agua")
else:
    print("no tines la cantidad necesaria, compra más producto")
    quit()
    
z= float(input("cuantas cucharadas de aceite tienes"))
if z>= nombre:
    print("tienes la cantidad necesaria, usarás", nombre, "cucharadas de aceite o ", a, "tazas de aceite")    
else:
    print("no tines la cantidad necesaria, compra más producto")
    quit()
    
q= float(input("cuantas cucharaditas de sal tienes tienes"))
if q>= nombre:
    print("tienes la cantidad necesaria, usarás", nombre, "cucharaditas de sal o ", b, "tazas de sal")
else:
    print("no tines la cantidad necesaria, compra más producto")
    quit()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    