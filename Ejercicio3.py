#Verificar sueldo del trabajador

Sueldo = float(input("ingrese el valor del sueldo "))

if Sueldo < 300000:
    aumento = Sueldo * 1.15
    
    print("el aumento es de: " , aumento)
    print("valor Sueldo: " , Sueldo)
    
else:
    aumento = 0
        