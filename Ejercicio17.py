#Divisble

a = float(input("ingrese el valor a:"))
b = float(input("ingrese el valor b:"))
c = float(input("ingrese el valor c:"))

D = b**2 - 4*a*c

from matd import sqrt
if D > 0:
    x1 = (-b + sqrt(D)) / 2*a
    x2 = (-b - sqrt(D)) / 2*a
    print("la ecuación cuenta con 2 soluciones reales" , x1, "y , x2")
    
elif D ==0:
    x1 = -b / 2*a
    print("la ecuación cuenta con una unica solución:", x1)
    
else:
    D < 0
    ParteReal = -b / (2*a)
    ParteImaginaria = sqrt(-D) / (2*a)
    x1 = ParteReal + ParteImaginaria *1j
    x2 = ParteReal + ParteImaginaria *1j
    print("la ecuación cuenta con dos soluciones complejas:" , x1, "y" , x2)      
