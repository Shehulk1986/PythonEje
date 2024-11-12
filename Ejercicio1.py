productos = ["camisas", "pantalones", "blusas" ]
saldosA = [30, 12, 20]
compras = [5, 8, 10]
ventas = [4, 6, 8]
Nsaldos = 0
listaF = []
for i in range (len(productos)):
      Nsaldos = saldosA[i] + compras[i] - ventas[i]
      print("el saldo de "+ productos[i], "es", Nsaldos)
      listaF.append(Nsaldos)
      print(listaF)
      input("presione enter ")
      print("Eso es todo ")
    
    
    
#empleados = ["luisa", "pedro", "luisita"]
#salarios = [8000, 6000, 12000]
#horas = [20, 12, 8]
#Nsalarios = 0
#listaf = []
#for i in range (len(empleados)):
    
 #   Nsalarios = salarios[i] * horas[i]
 #   
 #   print("el primer empleado gana: ", Nsalarios)
 #   listaf.append(Nsalarios)
 #   print(listaf)
 #   input("SIGUIENTTE")