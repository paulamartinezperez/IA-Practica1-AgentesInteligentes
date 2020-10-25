import sys
import numpy as np
from random import randrange

MATRIZ = [["0","0","0","0","0"],
          ["0","0","0","0","0"],
          ["0","0","0","0","0"],
          ["0","0","0","0","0"],
          ["0","0","0","0","0"]]

## LEEMOS EL ARCHIVO QUE CONTIENE EL MAPA
def matriz_leer():
##MATRIZ[0-4][0-4]
## por ejemplo para ir a la posicion X de la fila 5 y columna 4 sería MATRIZ[4][3]
    cadena = open('map.txt')
    x = 0
    y = 0
    for caracter in cadena:
        a = caracter.split()
        for i in a:
            MATRIZ[y][x] = i
            x += 1
        x = 0
        y += 1

## DIBUJAMOS EN EL TERMINAL EL ESCENARIO
def dibujar_escenario():
    for y in range(5):
        for x in range(5):
            print(MATRIZ[y][x], end=" ")
        print("\n")

## OPTENEMOS UNA POSICION INICIAL ALEATORIA PARA EL ROBOT
def pos_robot_aleatoria():
    pos_x = randrange(5)
    pos_y = randrange(5)

    while(MATRIZ[pos_y][pos_x] == "X"):
        pos_x = randrange(5)

    return pos_x, pos_y


def percencion(x, y):
    pos_actual = MATRIZ[x][y];

    if(y == 0):
        izquierda = "X";
    else:
        izquierda =  MATRIZ[x][y-1];

    if( x == 0):
        arriba = "X";
    else:
        arriba = MATRIZ[x-1][y];

    if(y == 4):
        derecha = "X"
    else:
        derecha = MATRIZ[x][y+1]
    if(x == 4):
        abajo = "X"
    else:
        abajo = MATRIZ[x+1][y]

    return pos_actual,izquierda,arriba,derecha,abajo


def salida_inicial(x,y,actual,izq,arri,der,abaj):
    print("Initial position: <",x,",",y,">  Perception: <",actual,",",izq,",",arri,",",der,",",abaj,">")



matriz_leer()
dibujar_escenario()
x_robot , y_robot = pos_robot_aleatoria()
pos_actual,izquierda,arriba,derecha,abajo = percencion(x_robot,y_robot)
salida_inicial(x_robot, y_robot, pos_actual, izquierda, arriba, derecha, abajo)
