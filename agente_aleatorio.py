import sys
import numpy as np

MATRIZ = [["0","0","0","0","0"],
          ["0","0","0","0","0"],
          ["0","0","0","0","0"],
          ["0","0","0","0","0"],
          ["0","0","0","0","0"]]

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


def dibujar_escenario():
    for y in range(5):
        for x in range(5):
            print(MATRIZ[y][x], end=" ")
        print("\n")


matriz_leer()
dibujar_escenario()
