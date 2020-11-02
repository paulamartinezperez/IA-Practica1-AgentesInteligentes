import sys
import numpy as np
import time
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

def escenario_limpio():
    limpio = True
    for y in range(5):
        for x in range(5):
            if(MATRIZ[y][x] == "1"):
                 limpio = False
    return limpio

def randomAction():
    ##---{UP, DOWN, RIGHT, LEFT, SUCK, NOOP}
    ##---{0, 1, 2, 3, 4, 5}
    action_ = randrange(6)

    if action_ == 0:
        accion_aleatoria = "UP"
    elif action_ == 1:
        accion_aleatoria = "DOWN"
    elif action_ == 2:
        accion_aleatoria = "RIGHT"
    elif action_ == 3:
        accion_aleatoria = "LEFT"
    elif action_ == 4:
        accion_aleatoria = "SUCK"
    elif action_ == 5:
        accion_aleatoria = "NOOP"

    return accion_aleatoria


class Robot:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def percencion(self):
        self.pos_actual = MATRIZ[self.pos_x][self.pos_y];

        if(self.pos_y == 0):
            self.izquierda = "X";
        else:
            self.izquierda =  MATRIZ[self.pos_x][self.pos_y-1];

        if( self.pos_x == 0):
            self.arriba = "X";
        else:
            self.arriba = MATRIZ[self.pos_x-1][self.pos_y];

        if(self.pos_y == 4):
            self.derecha = "X"
        else:
            self.derecha = MATRIZ[self.pos_x][self.pos_y+1]
        if(self.pos_x == 4):
            self.abajo = "X"
        else:
            self.abajo = MATRIZ[self.pos_x+1][self.pos_y]



    def salida_inicial(self):
        print("Initial position: <",self.pos_x,",",self.pos_y,">  Perception: <",
                self.pos_actual,",",self.izquierda,",",self.arriba,",",self.derecha,",",self.abajo,">")


    def movimiento_accion(self):
        accion = randomAction()
        while ((accion == "UP" and self.pos_x == 0) or (accion == "DOWN" and self.pos_x == 4) or (accion == "RIGHT" and self.pos_y == 4)
                or (accion == "LEFT" and self.pos_y == 0) or (accion == "SUCK" and self.izquierda == "0") or (accion == "UP" and self.arriba == "X")
                or (accion == "DOWN" and self.abajo == "X") or (accion == "RIGHT" and self.derecha == "X") or (accion == "LEFT" and self.izquierda == "X")):
            accion = randomAction()
        self.action = accion

    def do_action(self):
        if self.action == "UP":
            self.pos_x = self.pos_x - 1
        elif self.action == "DOWN":
            self.pos_x = self.pos_x + 1
        elif self.action == "RIGHT":
            self.pos_y = self.pos_y + 1
        elif self.action == "LEFT":
            self.pos_y = self.pos_y - 1
        elif self.action == "SUCK":
            MATRIZ[self.pos_x][self.pos_y] = "0";



    def salida_secuencia_acciones(self):
        print("State <",self.pos_x,",",self.pos_y,">  Perception: <",self.pos_actual,
                ",",self.izquierda,",",self.arriba,",",self.derecha,",",self.abajo,"> Action:",self.action)



#---------------------------- MAIN // PROGRMA PRINCIPAL ------------------------------------------------------·#

matriz_leer()
dibujar_escenario()


robot1 = Robot(0,0)
robot1.percencion()
robot1.salida_inicial()

iniciar = escenario_limpio()
print(iniciar)

while iniciar == False:
    robot1.movimiento_accion()
    robot1.do_action()
    robot1.percencion()
    robot1.salida_secuencia_acciones()
    iniciar = escenario_limpio()
    #time.sleep(1)
dibujar_escenario()
