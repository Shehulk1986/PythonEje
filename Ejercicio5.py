#Leer un numero

Num1 = int(input("digite primer número: "))
Num2 = int(input("digite segundo número: "))
Num3 = int(input("digite tercer número: "))

mayor = max (Num1,Num2,Num3)
menor = min (Num1,Num2,Num3)

print(f"el numero mayor es: {mayor}")
print(f"el número menor es: {menor}")

if Num1 == Num2 == Num3:
    print("los tres números son iguales.")
    
elif Num1 == Num2 or Num1 == Num3 or Num2 == Num3:
    print("hay dos números iguales")
    
else:
    print("los tres números son diferentes")
    
