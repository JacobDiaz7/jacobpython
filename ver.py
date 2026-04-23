def suma():
    num=int(input("Ingrese un numero: "))
    num2=int(input("Ingrese un segundo numero: "))
    print(f"el total de la suma es de {num+num2}")
def resta():
    num=int(input("Ingrese un numero: "))
    num2=int(input("Ingrese un segundo numero: "))
    print(f"el total de la resta es de {num-num2}")
def multiplicacion():
    num=int(input("Ingrese un numero: "))
    num2=int(input("Ingrese un segundo numero: "))
    print(f"el total de la multiplicacion es de {num*num2}")
def division():
    num=int(input("Ingrese un numero: "))
    num2=int(input("Ingrese un segundo numero: "))
    print(f"el total de la division es de {num/num2}")


op=0

while op!=5:
    print("1.- Sumar ambos numeros")
    print("2.- restas numeros")
    print("3.- multiplicar numeros")
    print("4.- dividir numeros")
    print("5.- salir")
    op=int(input())
    match op:
        case 1:
            suma()
        case 2:
            resta()
        case 3:
             multiplicacion()
        case 4:
            division()
        case 5:
            print("saliendo del programa")
        case _:
            print("opcion invalida")
