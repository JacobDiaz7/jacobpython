# op=0
# cantP=0
# total=0
# while op!=4:
#     print('''
#         Menu de entradas:
#         1.- Niño (1-17) $1.000
#         2.- Adulto (18-64) $3.000
#         3.- Adulto mayor (64 o mas) $1.500
#         4.- Salir y mostrar total a pagar''')
#     op=int(input("seleccione una opcion "))
#     match op:
#         case 1:
#             cantn=int(input("Cuantos niños son?: "))
#             while cantn<1 or cantn>10:
#                 print("Cantidad fuera de rango (1-10)")
#                 cantn=int(input("Cuantos niños son?: "))
#             print("se han agregado las entradas de niños")
#             total=total+(cantn*1000)
#             cantP=cantP+cantn
#         case 2:
#             cantA=int(input("cuantos adultos son?: "))
#             while cantA<1 or cantA>10:
#                 print("cantidad fuera de rango (1-10)")
#                 cantA=int(input("cuantos adultos son?: "))
#             print("se han agregado las entradas de adulto")
#             total=total+(3000*cantA)
#             cantP=cantP+cantA
#         case 3:
#             cantAM=int(input("cuantos adultos mayores son?: "))
#             while cantAM<1 or cantAM>10:
#                 print("cantidad fuera de rango (1-10)")
#                 cantAM=int(input("cuantos adultos mayores son?: "))
#             print("se han agregado las entradas de adulto mayor")
#             total=total+(1500*cantAM)
#             cantP=cantP+cantAM
#         case 4:
#             print("Saliendo del menu")
#             print(f"el total a pagar es de {total*1.19} el total de personas que entraran es de {cantP}")
#         case _:
#             print("opcion invalida")

# import random

# num=random.randint(7000-21000)
# print(num)
# op=0
# total=0
# while op!=4:
#     print('''
#         Menu de entradas:
#         1.- Entrada Tribuna
#         2.- Entrada Cancha genral
#         3.- Cancha VIP
#         4.- Salir y ver el total
#         ''')
#     op=int(input("Seleccione una opcion"))
#     match op:
#         case 1:
#             cantT=int(input("Cuantas entradas de Tribuna comprara?: "))
#             print(f"se han añadido {cantT} entradas")
#             total=total+(cantT(40000*1.2))
#         case 2:
#             cantCG=int(input("Cuantas entradas de cancha general comprara?: "))
#             print(f"Se han añadido {cantCG} en el carro")
#             total=total+(cantCG(40000*1.4))
#         case 3:
#             cantVIP=int(input("Cuantas entradas VIP comprara?: "))
#             print(f"se han añadido {cantVIP} al carro")
#             total=total+(cantVIP(40000*1.8))
#         case 4:
#             print("salir del menu y ver el total a pagar")
#         case _:
#             print("opcion invalida")
# if code>7000 or code<12000:
#     print("Tiene un codigo de descuento aplicable")
#     print(f"el total a pagar es de {total*0.90}")
# else:
#     print(f"su total a pagar es de {total}")




