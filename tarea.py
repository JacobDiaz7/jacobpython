def promedio():
    num1=float(input("Ingrese su primera nota: "))
    num2=float(input("Ingrese su segunda nota: "))
    num3=float(input("Ingrese su tercera nota: "))
    print(f"el promedio es de {((num1+num2+num3)/3)}")
def vocales():
    nombre=input("Ingrese un nombre: ")
    vocales=0
    for i in nombre:
        if i in "aeiouAEIOU":
            vocales+=1
    print(f"la cantidad de vocales en el nombre es de {vocales}")
def letras():
    nombre=input("Ingrese un nombre: ")
    print(f"la cantidad de letras en el nombre es de {len(nombre)}")



op=0
while op!=4:
    print("1.- sacar promedio")
    print("2.- cantidad vocales en un nombre")
    print("3.- cantidad letras en un nombre")
    print("4.- salir")
    op=int(input())
    match op:
        case 1:
            promedio()
        case 2:
            vocales()
        case 3:
            letras()
        case 4: 
            print("saliendo del programa")
        case _:
            print("opcion no valida")