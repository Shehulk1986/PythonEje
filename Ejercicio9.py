# Ingreso de números a.b.c

a = int(input("ingrese primer número: "))
b = int(input("ingrese segundo número: "))
c = int(input("ingrese tercer número: "))

#Ordenar

if a >= b and a >= c:
    if b >= c:
        orden = [a,b,c]
    else:
        orden = [a,c,b]
elif b >=a and b >= c:
    if a >= c:
        orden = [b,c,a]
    else:
        orden = [b,c,a]
else:
    if a >= b:
        orden = [c,a,b]

print("Números ordenados de mayor a menor: ", orden)

  