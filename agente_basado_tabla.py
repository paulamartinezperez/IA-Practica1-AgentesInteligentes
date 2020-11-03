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
    cadena = open('map_agente_basado_tabla.txt')
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


    def tabla_accion(self):
        table = {
            (0, 0, '0') : 'RIGHT' ,
            (0, 0, '1') : 'SUCK'  ,
            (0, 1, '0') : 'DOWN'  ,
            (0, 1, '1') : 'SUCK'  ,
            (0, 2, '0') : 'LEFT'  ,
            (0, 2, '1') : 'SUCK'  ,
            (0, 3, '0') : 'LEFT'  ,
            (0, 3, '1') : 'SUCK'  ,
            (0, 4, '0') : 'DOWN'  ,
            (0, 4, '1') : 'SUCK'  ,
            (1, 0, '0') : 'RIGHT' ,
            (1, 0, '1') : 'SUCK'  ,
            (1, 1, '0') : 'RIGHT' ,
            (1, 1, '1') : 'SUCK'  ,
            (1, 2, '0') : 'DOWN'  ,
            (1, 2, '1') : 'SUCK'  ,
            (1, 3, '0') : 'UP'    ,
            (1, 3, '1') : 'SUCK'  ,
            (1, 4, '0') : 'DOWN'  ,
            (1, 4, '1') : 'SUCK'  ,
            (2, 0, '0') : 'DOWN'  ,
            (2, 0, '1') : 'SUCK'  ,
            (2, 1, '0') : 'RIGHT' ,
            (2, 1, '1') : 'SUCK'  ,
            (2, 2, '0') : 'DOWN'  ,
            (2, 2, '1') : 'SUCK'  ,
            (2, 3, '0') : 'LEFT'  ,
            (2, 3, '1') : 'SUCK'  ,
            (2, 4, '0') : 'LEFT'  ,
            (2, 4, '1') : 'SUCK'  ,
            (3, 0, '0') : 'DOWN'  ,
            (3, 0, '1') : 'SUCK'  ,
            (3, 1, '0') : 'UP'    ,
            (3, 1, '1') : 'SUCK'  ,
            (3, 2, '0') : 'RIGHT' ,
            (3, 2, '1') : 'SUCK'  ,
            (3, 3, '0') : 'RIGHT' ,
            (3, 3, '1') : 'SUCK'  ,
            (3, 4, '0') : 'DOWN'  ,
            (3, 4, '1') : 'SUCK'  ,
            (4, 0, '0') : 'UP'    ,
            (4, 0, '1') : 'SUCK'  ,
            (4, 1, '0') : 'UP'    ,
            (4, 1, '1') : 'SUCK'  ,
            (4, 2, '0') : 'LEFT'  ,
            (4, 2, '1') : 'SUCK'  ,
            (4, 3, '0') : 'LEFT'  ,
            (4, 3, '1') : 'SUCK'  ,
            (4, 4, '0') : 'LEFT'  ,
            (4, 4, '1') : 'SUCK'  ,
        }

        print(table[(self.pos_x, self.pos_y, MATRIZ[self.pos_x][self.pos_y])])

        self.action = table[(self.pos_x, self.pos_y, MATRIZ[self.pos_x][self.pos_y])]

    def do_action(self):
        if self.action == "UP":
            if(MATRIZ[self.pos_x-1][self.pos_y] == 'X' and self.pos_y < 4):
                self.action = "RIGHT"
            elif (MATRIZ[self.pos_x-1][self.pos_y] == 'X' and self.pos_y == 4):
               self.action = "LEFT"
            else :
                self.pos_x = self.pos_x - 1
        elif self.action == "DOWN":
            if(MATRIZ[self.pos_x+1][self.pos_y] == 'X' and self.pos_y < 4 ):
                self.action = "RIGHT"
            elif (MATRIZ[self.pos_x+1][self.pos_y] == 'X' and self.pos_y == 4):
               self.action = "LEFT"
            else :
                self.pos_x = self.pos_x + 1
        elif self.action == "RIGHT":
            if(MATRIZ[self.pos_x][self.pos_y +1] == 'X' and self.pos_x < 4):
                self.pos_x = self.pos_x + 1
            elif (MATRIZ[self.pos_x][self.pos_y +1] == 'X' and self.pos_x == 4):
                self.pos_x = self.pos_x - 1
            else :
                self.pos_y = self.pos_y + 1
        elif self.action == "LEFT":
            if(MATRIZ[self.pos_x][self.pos_y -1] == 'X' and self.pos_x < 4):
                self.pos_x = self.pos_x + 1
            elif (MATRIZ[self.pos_x][self.pos_y -1] == 'X' and self.pos_x == 4):
                self.pos_x = self.pos_x - 1
            else :
                self.pos_y = self.pos_y - 1
        elif self.action == "SUCK":
            MATRIZ[self.pos_x][self.pos_y] = "0";



    def salida_secuencia_acciones(self):
        print("State <",self.pos_x,",",self.pos_y,">  Perception: <",self.pos_actual,
                ",",self.izquierda,",",self.arriba,",",self.derecha,",",self.abajo,"> Action:",self.action)

    def alrededor_limpio(self):
        limpio = True
        if(self.pos_actual == '1' or self.izquierda == '1' or self.derecha == '1' or self.arriba == '1' or self.abajo == '1'):
            limpio = False
        return limpio


#---------------------------- MAIN // PROGRMA PRINCIPAL ------------------------------------------------------·#

matriz_leer()
dibujar_escenario()


robot1 = Robot(0,0)
robot1.percencion()
robot1.salida_inicial()

iniciar = robot1.alrededor_limpio()
print(iniciar)

while iniciar == False:
    robot1.tabla_accion()
    robot1.do_action()
    robot1.percencion()
    robot1.salida_secuencia_acciones()
    iniciar = robot1.alrededor_limpio()
    dibujar_escenario()
    time.sleep(0.5)

print("Bye, execution finished")
