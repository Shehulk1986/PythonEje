#Capturar notas

nota1 = float(input("ingrese la primera nota(0-5): "))
nota2 = float(input("ingrese la segunda nota(0-5): "))
nota3 = float(input("ingrese la tercera nota(0-5): "))

if nota1 <= nota2 and nota1 <=nota3:
    promedio_final =(nota2+nota3)/2
    
elif nota2 <= nota1 and nota2 <= nota3:
    promedio_final =(nota1+nota3)/2

else:
    promedio_final = (nota1+nota2)/2
    
    print(f"su nota final es: {promedio_final:.2f}")    
    