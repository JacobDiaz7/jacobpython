# uso y ejemplo de random

import random ; import time

# num=random.randint(1,10)
# print(num)

# for i in range(num):
#     print("Hola deny")


# dado1=random.randint(1,6)
# dado2=random.randint(1,6)

# print(f"el dado 1 dio {dado1}")
# print(f"el dado 2 dio {dado2}")

# if dado1==dado2:
#     print("se va a la carcel")
# else:
#     print("avance por favor")

# numA=random.randint(1,100)

# for i in range(5):
#     num=int(input("Ingrese un numero: "))
#     if num>numA:
#         print("te pasaste")
#     elif num<numA:
#         print("el numero adivinar es mayor")
#     elif num==numA:
#         print("adivinaste el numero")
#         break
# if num!=numA:
#     print(f"perdiste se acabaron tus intentos, el numero adivinar era {numA}")


import random ; import time

# golpe=random.randint(7,18)


# name1=input("Ingrese el nombre del jugador 1")
# name2=input("ingrese el nombre del jugador 2")
# p1=100
# p2=100

# while p1>=0 and p2>=0:
#     golpe=random.randint(7,18)
#     print(f"el jugador 1 golpeo al jugador 2 le quito {golpe}")
#     p2=p2-golpe
#     time.sleep(2)
#     golpe=random.randint(7,18)
#     print(f"el jugador 2 golpeo al jugador 1 le quito {golpe}")
#     p1=p1-golpe
#     time.sleep(2)
#     if p1==0:
#         print("el jugador 2 gano")
#     elif p2==0:
#         print("el jugador 1 gano")
    



# n1=random.randint(1,9)
# n2=random.randint(1,9)
# n3=random.randint(1,9)
# num=0
# print(f"sus numeros de loteria son {n1, n2, n3}")

# while num!=n1 or num!=n2 or num!=n3:
    
#     print(f"el numero que salio en esta tirada fue {num}")
#     num=random.randint(1,9)
#     time.sleep(2)
#     if num==n1:
#         print("tiene su primer numero")
#     elif num==n2:
#         print("tiene su segundo numero")
#     elif num==n3:
#         print("tiene su tercer numero")
#         print(f"felicidades salieron todos tus numeros ganaste el premio")


# n1=random.randint(1,9)
# n2=random.randint(1,9)
# n3=random.randint(1,9)
# t1=False
# t2=False
# t3=False
# nums=0
# print(f"sus numeros de loteria son: {n1, n2, n3}")

# while not t1 or not t2 or not t3:
#     num=random.randint(1,9)
#     print(f"El numero es {num}")
#     time.sleep(1)
#     if num==n1:
#         t1=True
#     if num==n2:
#         t2=True
#     if num==n3:
#        t3=True
#     nums+=1
# print(f"ganaste en {nums} turnos")

# gr=int(input("cual es el peso del producto en gramos: "))
# sd=float(input("que porcentaje de sodio tiene el producto: "))
# nv=int(input("Ingres 1 si desea envio nacional o 2 para envio enternacional: "))

# if gr<500:
#     print("la lata del producto es una pequeña")
# elif gr>501 and gr<1501:
#     print("la lata del producto debe ser mediana")
# elif gr>1500:
#     print("la lata de su producto debe ser grande")
    
# if sd<5:
#     print("la lata debe ser igual")
# elif sd==5 and sd>8:
#     print("el nivel de sodio es mas alto y necesita una lata especial")
# elif sd<=9:
#     print("se necesita una lata acorazada")

# if nv==1:
#     print("su envio es a nivel nacional")
# elif nv==2:
#     print("su producto necesita un sello para el envio internacional")
# else:
#     print("opcion no valida")
