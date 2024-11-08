#Notas Sena

Nota_evaluativa = float(input("ingrese nota evaluativa: "))
Nota_trabajos =  float(input("ingrese nota de trabajos: "))
Nota_quiz = float(input("ingrese nota de quiz:" ))

Nota_total = (Nota_evaluativa*0.4)+(Nota_trabajos*0.3)+(Nota_quiz*0.3)

if Nota_total>= 3.0:
    print("pasaste la materia")
    print("Nota total:",Nota_total)
    
elif 2.5 <= Nota_total<3.0:
    print("presentar examen de recuperación")
    print("Nota total:", Nota_total)

else:
    print("No aprobaste la materia")
    print("Nota total:",Nota_total)