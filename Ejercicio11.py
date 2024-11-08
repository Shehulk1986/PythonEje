# Longitud y diametro

longitud = float(input("ingrese longitud de la pieza: "))
diametro = float(input("ingrese diametro de la pieza: ")) 

masa = (diametro*longitud)/3.5

if(7.5<longitud<=9)and(0.5 <= diametro <= 1.3) and (masa <= 5.8):
   
    print("pieza aceptada")
    
else:
    print("pieza rechazada")
    
