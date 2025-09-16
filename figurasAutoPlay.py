"""pratica-
Irma Patricia Rivera León
"""

import turtle as t
from random import random

radio = 50
num_lados = 360
angulo_giro = 360 / num_lados
avance = (2 * 3.14159 * radio) / num_lados


def teleport(x: float,y:float)-> None:
    t.penup()
    t.setx(x)
    t.sety(y)
    t.pendown()


#Acomodo inicial
teleport(0,0)


#Cuadrado azul 0,0,255
t.pencolor("blue")
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)


#Triángulo rojo 255,0,0
teleport(50, 0)
t.pencolor("red")
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)


#Círculo verde 0,255,0
teleport(-100,-100)
t.pencolor("green")
teleport(50,-100)
for _ in range(num_lados):
    t.forward(avance)
    t.left(angulo_giro)



#Línea yellow 255,255,0
teleport(-50,-50)
t.setheading(90)
t.pencolor("yellow")
t.right(180)
t.forward(120)



#Tortuga se queda esperando
t.done()
