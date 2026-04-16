
# for i in range(3):
#     print("repeticion N", i+1)

#

# num=int(input("INGRESE UN NUMERO: "))
# for i in range(num):
#     print(i+1, "Hola usuario")


# num=int(input("INGRESE UN NUMERO: "))
# for i in range(10):
#     print(num, "X", i, num*i )


# num=int(input("INGRESE la cant de notas: "))
# suma=0
# for i in range (num):
#     nota=float(input("Ingrese la nota: "))
#     suma=suma+nota
# prom=suma/num
# print("el promedio es", prom)
# if prom>=4:
#     print("el alumno aprob")
# else:
#     print("el alumno reprobo")


# nombre=input ("Ingrese su nombre")
# cantLetra=0
# for i in "nombre":
#     print(i)
#     cantLetra=cantLetra+1
# print("La cantidad de caracteres es", cantLetra)

# cantN=int(input("Cuantas notas tiene? "))
# suma=0
# for i in range (cantN):
#     nota=float(input(f"Ingrese su nota {i+1}: "))
#     suma=suma+nota
# prom=suma/cantN
# print("El promedio es",round (prom, 1))
# if prom>=4:
#     print("el alumno aprob")
# else:
#     print("el alumno no aprob")

# cantA=int(input("cuantos alumnos son? "))

# name=input ("Ingrese su nombre: ")
# cantLetra=0
# for i in name:
#     print(i)
#     cantLetra=cantLetra+1
# print(f"La cantidad de caracteres es {cantLetra}")

name=input ("Ingrese su nombre: ")
cantLetra=0
consonante=0
for i in name:
    print(i)
    if i in "AEIOUaeiou":
        cantLetra+=1
    elif i==" ":
        print()
    else:
        consonante+=1
print(f"La cantidad de caracteres es {cantLetra} y las consonantes son {consonante}")

