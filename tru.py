# while True:
#     try:
#         num=int(input("Ingrese un numero: "))
#     except ValueError as er:
#         print("ERROR", er)
#         print("solo debe ingresar numeros enteros")
#     else:
#         print("correcto")


# op=0
# total=0
# while op!=4:
#     try:
#         print("1.- PC 500.000")
#         print("2.- LGTV 55 PULGADAS 450.000")
#         print("3.- Microondas 100.000")
#         print("4.- salir")
#         print("Seleccione una opcion")
#         op=int(input())
#     except ValueError as e:
#         print("error", e)
#         print("solo se acepta numeros enteros")
#     match op:
#         case 1:
#             print("total a pagar es ", 500.000*1.19)
#             total+=500000*1.19
#         case 2:
#             print("total a pagar es ", 450.000*1.19)
#             total+=450000*1.19
#         case 3: 
#             print("total a pagar es ", 100.000*1.19)
#             total+=100000*1.19
#         case 4: 
#             print("total a pagar es ")


# while True:
#     try:
#         notas=int(input("Ingrese la cant de notas; "))
#         break
#     except ValueError as e:
#         print("error", e)
#         print("solo numeros enteros")

# suma=0
# for i in range(notas):
#     while True:
#         try:
#             n=float(input(f"ingrese la nota {i+1}: "))
#             break
#         except ValueError as e:
#             print("solo numero decimales")
#         suma=suma+n
#         prom=suma/notas
# print("el promedio es", round(prom,1))
    

# if prom>4:
#         print("alumo aprobado")
# else:
#         print("el alumno reprobo")

while True:
    try:
        pas=int(input("Cuantos pasajes desea llevar: "))
        break
    except ValueError as e:
        print("Error", e)
        print("Solo numeros enteros")
total=0
for i in range(pas):
    while True:
        try:
            precio=int(input("Cuanto vale el pasaje: "))
            break
        except ValueError as e:
            print("Error", e)
            print("Solo numeros enteros")
    total=total+precio
print(f"El precio total a pagar es de {total}")


