#Irma Patricia Rivera León

#Menú de opciones
print("Ingresa la figura que quieres dibujar")
print("1 Cuadro")
print("2 Triángulo")
print("3 Círculo")
print("4 Línea")

#Opción es el input como variable dentro de un case
opcion = int(input("Escribe el número de la figura: "))

def figura_a_dibujar(opcion):
    match opcion:
        case 1:
            return "Cuadrado"
        case 2:
            return "Triángulo"
        case 3:
            return "Círculo"
        case 4:
            return "Línea"
        case _:  # Caso por defecto
            return "Número inválido, intente de nuevo"
        
#Variable que guarda la figura del usuario y lo confirma
figura = figura_a_dibujar(opcion)
print("Seleccionaste:", figura)


import turtle as t
from random import random

#Función para dibujar el cuadrado
if figura == "Cuadrado":
    lado = int(input("Ingresa la longitud del lado: "))
    color = input("Ingresa el color en inglés: ")
    t.color(color)
    for i in range(4):
        t.forward(lado)
        t.right(90)

#Función para dibujar el triángulo
elif figura == "Triángulo":
    lado = int(input("Ingresa la longitud del lado: "))
    color = input("Ingresa el color en inglés: ")
    t.color(color)
    for i in range(3):
        t.forward(lado)
        t.left(120)

#Función para dibujar el círculo
elif figura == "Círculo":
    radio = int(input("Ingresa el radio del círculo: "))
    color = input("Ingresa el color en inglés: ")
    t.color(color)
    t.circle(radio)

#Función para dibujar la línea
elif figura == "Línea":
    longitud = int(input("Ingresa la longitud de la línea: "))
    color = input("Ingresa el color en inglés: ")
    t.color(color)
    t.forward(longitud)

#El mono termina de dibujar y se queda en espera
t.done()


