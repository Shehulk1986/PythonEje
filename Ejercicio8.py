#Conjunto de numeros

Num1 = int(input("digite el primer número: "))
Num2 = int(input("digite el segundo núnmero: "))
Num3 = int(input("digite el tercer número: "))

if  Num1 > Num2:
    mayor = Num1
    menor = Num2

else:
    mayor = Num2
    menor = Num1

if mayor < Num3:
    medio = mayor 
    mayor = Num3
    
else:
    medio = Num3

if menor > medio:
    medio = menor
    
print("El número medio es: " , medio)
