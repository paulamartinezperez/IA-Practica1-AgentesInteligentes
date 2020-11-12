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
        cadena = open('map.txt')
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

    ##añadimos el numero de obstaculos que queremos
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

    def escenario_limpio(self):
        limpio = True
        for y in range(5):
            for x in range(5):
                if(self.matriz[y][x] == "1"):
                     limpio = False
        return limpio

#------------------------------------------------------------------------------------------------------------

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

#----------------------------------------------------------------------------------------------------------------

class Robot:
    def __init__(self, pos_x, pos_y, matriz):
        #inicializamos el robot con su posicion en el mapa
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.matriz = matriz

    def percencion(self):
        #obtemenos la percepcion que tiene el robot a su alrededor
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
        #salida por terminal inicial
        print("Initial position: <",self.pos_x,",",self.pos_y,">  Perception: <",
                self.pos_actual,",",self.izquierda,",",self.arriba,",",self.derecha,",",self.abajo,">")


    def movimiento_accion(self):
        ##agente de forma aleatoria_: escogemos la accion que debe de hacer de forma aleatoria sin tener en cuenta su alrededor
        accion = randomAction()
        while ((accion == "UP" and self.pos_x == 0) or (accion == "DOWN" and self.pos_x == 4) or (accion == "RIGHT" and self.pos_y == 4)
                or (accion == "LEFT" and self.pos_y == 0) or (accion == "SUCK" and self.izquierda == "0") or (accion == "UP" and self.arriba == "X")
                or (accion == "DOWN" and self.abajo == "X") or (accion == "RIGHT" and self.derecha == "X") or (accion == "LEFT" and self.izquierda == "X")):
            accion = randomAction()
        self.action = accion

    def do_action(self):
        ## mandamos la orden que hemos decidido hacer de forma aleatoria
        if self.action == "UP":
            self.pos_x = self.pos_x - 1
        elif self.action == "DOWN":
            self.pos_x = self.pos_x + 1
        elif self.action == "RIGHT":
            self.pos_y = self.pos_y + 1
        elif self.action == "LEFT":
            self.pos_y = self.pos_y - 1
        elif self.action == "SUCK":
            self.matriz[self.pos_x][self.pos_y] = "0";


    def salida_secuencia_acciones(self):
        #salida por termial de la ejecución del programa
        print("State <",self.pos_x,",",self.pos_y,">  Perception: <",self.pos_actual,
                ",",self.izquierda,",",self.arriba,",",self.derecha,",",self.abajo,"> Action:",self.action)



#---------------------------- MAIN // PROGRMA PRINCIPAL ------------------------------------------------------·#
##creamos el mundo con los obstaculos que decidimos
environment = Environment()
num_muros = environment.numero_muros()
matriz = environment.matriz_leer()
environment.add_obstaculos()
environment.dibujar_escenario()

##creamos el agente
robot1 = Robot(0, 0, matriz)
robot1.percencion()
robot1.salida_inicial()

iniciar = environment.escenario_limpio()

##hasta que el escenario no esté limpio se ejecutara
## muchas veces queda en un bucle infinito ya que al ser aleatoria sin tener en
##cuenta nada del mundo las acciones no son las adecuadas
while iniciar == False:
    robot1.movimiento_accion()
    robot1.do_action()
    robot1.percencion()
    robot1.salida_secuencia_acciones()
    iniciar = environment.escenario_limpio()

print("Bye, execution finished")
