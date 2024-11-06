#Lectura de registros

nombre = input("ingrese el nombre: ")
edad = int(input("ingrese edad: "))
sexo = input("ingrese el sexo: (hombre/mujer): ").strip().lower()
estado_civil = input("ingrese el estado civil: ").strip().lower()

if sexo == "hombre" and estado_civil == "casado" and edad > 40:
    print(f"nombre: {nombre}")
elif sexo == "mujer" and estado_civil == "soltera" and edad < 50:
    print(f"nombre: {nombre}")  