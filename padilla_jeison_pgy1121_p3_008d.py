#comenzamos
import funciones as fn
import numpy
import os
import msvcrt
import random
import time

lista_rut=[]
lista_nombredueño=[]
lista_nombremascota=[]
lista_dias=[]
contador = 1
hospedaje = (1,2,3,4,5,6,7,8,9,10)
lista_habitacion=[]

print("Hola!, bienvenido a guardería Mascota segura")
print()
print("Menú: ")
print("1. Grabar")
print("2. Buscar")
print("3. Retirarse")
print("4. Salir")

while True:
    opcion = fn.validar_opcion()
    if opcion==1:
           lista_rut = fn.validar_rut()
           lista_nombredueño = fn.validar_nombre_dueño()
           lista_nombremascota = fn.validar_nombre_mascota()
           lista_dias = fn.validar_dias()
           habitacion = contador +1
           print("HABITACIONES:")
           print(hospedaje)
           lista_habitacion = fn.validar_habitacion()
    elif opcion==2:
       rut = fn.validar_rut()
       if rut in lista_rut:
           print("Nombre dueño:", lista_nombredueño)
           print("Nombre mascota:", lista_nombremascota)
           print("Habitación mascota:", lista_habitacion)
    elif opcion==3:
        rut = fn.validar_rut
        if rut in lista_rut:
            total = lista_dias * 15000
            print("Su total a pagar es: ", total)
        else:
            print("ERROR! El rut no se encuentra en la guardería!")
    else:
        print("Muchas gracias, hasta pronto!")
        break

