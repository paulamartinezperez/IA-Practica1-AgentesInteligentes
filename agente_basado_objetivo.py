import sys
import numpy as np
import time
from random import randrange



class Environment:
    def __init__(self):
        self.matriz = [["0","0","0","0","0"],
                       ["0","0","0","0","0"],
                       ["0","0","0","0","0"],
                       ["0","0","0","0","0"],
                       ["0","0","0","0","0"]]
        self.num_obstaculos = 0
    ## LEEMOS EL ARCHIVO QUE CONTIENE EL MAPA

    def numero_muros(self):
        print("Cuantos obstaculos quieres?")
        self.num_obstaculos = int(input())
        return self.num_obstaculos


    def matriz_leer(self):
    ##MATRIZ[0-4][0-4]
    ## por ejemplo para ir a la posicion X de la fila 5 y columna 4 sería MATRIZ[4][3]
        cadena = open('map_agente_aleatorio.txt')
        x = 0
        y = 0
        for caracter in cadena:
            a = caracter.split()
            for i in a:
                self.matriz[y][x] = i
                x += 1
            x = 0
            y += 1
        return self.matriz

    def add_obstaculos(self):
        for i in range(self.num_obstaculos) :
            pos_x_aleatoria = randrange(5)
            pos_y_aleatoria = randrange(5)
            while((self.matriz[pos_x_aleatoria][pos_y_aleatoria] == "X") or (pos_x_aleatoria == 0 and pos_y_aleatoria == 0)) :
                pos_x_aleatoria = randrange(5)
                pos_y_aleatoria = randrange(5)
            self.matriz[pos_x_aleatoria][pos_y_aleatoria] = "X"


    ## DIBUJAMOS EN EL TERMINAL EL ESCENARIO
    def dibujar_escenario(self):
        for y in range(5):
            for x in range(5):
                print(self.matriz[y][x], end=" ")
            print("\n")




#----------------------------------------------------------------------------------------------------------------

class Robot:
    def __init__(self, pos_x, pos_y, matriz):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.matriz = matriz


    def percencion(self):
        self.pos_actual = self.matriz[self.pos_x][self.pos_y];

        if(self.pos_y == 0):
            self.izquierda = "X";
        else:
            self.izquierda =  self.matriz[self.pos_x][self.pos_y-1];

        if( self.pos_x == 0):
            self.arriba = "X";
        else:
            self.arriba = self.matriz[self.pos_x-1][self.pos_y];

        if(self.pos_y == 4):
            self.derecha = "X"
        else:
            self.derecha = self.matriz[self.pos_x][self.pos_y+1]
        if(self.pos_x == 4):
            self.abajo = "X"
        else:
            self.abajo = self.matriz[self.pos_x+1][self.pos_y]


    def salida_inicial(self):
        print("Initial position: <",self.pos_x,",",self.pos_y,">  Perception: <",
                self.pos_actual,",",self.izquierda,",",self.arriba,",",self.derecha,",",self.abajo,">")


    def sucio_mas_cercano(self):
        x_mas_cerca = 10
        y_mas_cerca = 10
        for x in range(5) :
            for y in range(5):
                if(self.matriz[x][y] == "1") :
                    if(abs(self.pos_x - x) + abs(self.pos_y - y ) < abs(self.pos_x - x_mas_cerca) + abs(self.pos_y - y_mas_cerca)):
                        x_mas_cerca = x
                        y_mas_cerca = y
        self.pos_cercano_x = x_mas_cerca
        self.pos_cercano_y = y_mas_cerca


    def do_action(self):
        while(self.pos_x != self.pos_cercano_x or self.pos_y != self.pos_cercano_y) :
            if(self.pos_x > self.pos_cercano_x) :
                self.pos_x = self.pos_x - 1
                self.action = "UP"
            elif(self.pos_x < self.pos_cercano_x) :
                self.pos_x = self.pos_x + 1
                self.action = "DOWN"
            elif(self.pos_y > self.pos_cercano_y) :
                self.pos_y = self.pos_y - 1
                self.action = "LEFT"
            elif(self.pos_y < self.pos_cercano_y) :
                self.pos_y = self.pos_y + 1
                self.action = "RIGHT"

            self.pos_actual = self.matriz[self.pos_x][self.pos_y];

            if(self.pos_y == 0):
                self.izquierda = "X";
            else:
                self.izquierda =  self.matriz[self.pos_x][self.pos_y-1];

            if( self.pos_x == 0):
                self.arriba = "X";
            else:
                self.arriba = self.matriz[self.pos_x-1][self.pos_y];

            if(self.pos_y == 4):
                self.derecha = "X"
            else:
                self.derecha = self.matriz[self.pos_x][self.pos_y+1]
            if(self.pos_x == 4):
                self.abajo = "X"
            else:
                self.abajo = self.matriz[self.pos_x+1][self.pos_y]

            print("State <",self.pos_x,",",self.pos_y,">  Perception: <",self.pos_actual,
                    ",",self.izquierda,",",self.arriba,",",self.derecha,",",self.abajo,"> Action:",self.action)

    def limpiar_pos(self):

        self.matriz[self.pos_x][self.pos_y] = "0"
        if(self.pos_y == 0):
            self.izquierda = "X";
        else:
            self.izquierda =  self.matriz[self.pos_x][self.pos_y-1];

        if( self.pos_x == 0):
            self.arriba = "X";
        else:
            self.arriba = self.matriz[self.pos_x-1][self.pos_y];

        if(self.pos_y == 4):
            self.derecha = "X"
        else:
            self.derecha = self.matriz[self.pos_x][self.pos_y+1]
        if(self.pos_x == 4):
            self.abajo = "X"
        else:
            self.abajo = self.matriz[self.pos_x+1][self.pos_y]

        self.action = "SUCK"
        print("State <",self.pos_x,",",self.pos_y,">  Perception: <",self.pos_actual,
                ",",self.izquierda,",",self.arriba,",",self.derecha,",",self.abajo,"> Action:",self.action)


    def salida_secuencia_acciones(self):
        print("State <",self.pos_x,",",self.pos_y,">  Perception: <",self.pos_actual,
                ",",self.izquierda,",",self.arriba,",",self.derecha,",",self.abajo,"> Action:",self.action)

    def escenario_limpio(self):
        limpio = True
        for y in range(5):
            for x in range(5):
                if(self.matriz[y][x] == "1"):
                     limpio = False
        return limpio
#---------------------------- MAIN // PROGRMA PRINCIPAL ------------------------------------------------------·#
environment = Environment()
num_muros = environment.numero_muros()
matriz = environment.matriz_leer()
environment.add_obstaculos()
environment.dibujar_escenario()

robot1 = Robot(0, 0, matriz)
robot1.percencion()
robot1.salida_inicial()

iniciar = robot1.escenario_limpio()
while iniciar == False:
    robot1.sucio_mas_cercano()
    robot1.do_action()
    robot1.limpiar_pos()
    iniciar = robot1.escenario_limpio()

environment.dibujar_escenario()

print("Bye, execution finished")
