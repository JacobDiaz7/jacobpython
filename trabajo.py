# saldo=100000
# op=0

# while op!=4:
#     try:
#         print("menu de opciones")
#         print("1.- consultar saldo")
#         print("2.- retirar dinero")
#         print("3.- depositar dimero")
#         print("4.- salir")
#         op=int(input("Seleccione una opcion: "))
#     except ValueError as e:
#         print("ERORR")
#         print("SOLO NUMEROS ENTEROS DEL 1 AL 4")
#     match op:
#         case 1:
#             print(f"el saldo actual de la caja es de {saldo}")
#         case 2:
#             while True:
#                 try:
#                     sacar=int(input("Cuanto dinero desea sacar de la caja?: "))
#                     if sacar % 5000==0:
#                         print(f"el monto {sacar} es valido de retirar")
#                         saldo=saldo-sacar
#                         break
#                     else: 
#                         print(f"el monto {sacar} no es valido de retirar")
#                 except ValueError:
#                     print("opcion no valida")
#         case 3:
#             while True:
#                 try:
#                     ing=int(input("Cuanto dinero va a ingresar a la caja?: "))
#                     if ing % 5000==0:
#                         print(f"el monto {ing} es valido de ingresar")
#                         saldo=saldo+ing
#                         break
#                     else:
#                         print(f"el monto {ing} no es valido de ingresar")
#                 except ValueError:
#                     print("Opciion no valida")
#         case 4:
#             print("Saliendo de la caja, buen dia.")
#         case _:
#             print("Seleccione una opcion valida")
    