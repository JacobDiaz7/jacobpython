cred=-100000
op=0
while True:
    try:
        while op!=3:
            print("Menu")
            print("1.- pagar deuda / Ingresar dinero")
            print("2.- Menu de compras")
            print("3.- Salir")
            op=int(input("Seleccione una opcion: "))
            break
    except ValueError as e:
        print("ERROR")
        print("Solo numeros enteros")
    match op:
        case 1:
            print("usted tiene una deuda")
            while True:
                try:
                    mot=int(input("Cuanto desea recargar a su tarjeta: "))
                    while mot<0 and mot>abs(cred):
                        print(f"Su saldo actual es de {i+1}")
                    cred=cred+mot
                    break
                except ValueError:
                    print("ERROR INGRESE SOLO NUMEROS")
            print(f"su saldo actual de credito es de {cred}")
        case 2:
            try:
                com=int(input("Cuantos articulos comprara: "))
            except ValueError:
                print("ERROR")
            for i in range(com):
                try:
                    pre=int(input(f"Cuanto cuesta su art {i+1}: "))
                    while pre <=0:
                        pre=int(input(f"Cuanto cuesta su articulo?{i+1}: "))
                        break
                    cred=cred-pre
                except ValueError:
                    print("error")
                print(f"Su saldo actual ahora es de {cred}")
        case 3:
            print("saliendo del menu gracias vuelva nunca")
        case _:
            print("OPCION INVALIDA")