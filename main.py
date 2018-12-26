# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 21:38:55 2018
@author: enaut.genua
"""
import time
from casilla import Casilla
from casilla import numero
from casilla import mina
from Tablero import Tablero
matr = []
def levantar_auto(matr):
        for i in range(len(matr)):
            for j in range(len(matr[0])):
                if Casilla.get_lev(matr[i][j]) == True:
                    if Casilla.get_val(matr[i][j]) == 0:
                        if numero(i, j).analizar_minas(matr) == 0:
                            for x in range(max(i-1, 0), min(i+2, len(matr))):
                                for y in range(max(j-1, 0), min(j+2, len(matr))):
                                    Casilla.set_lev(matr[x][y], True)
        return matr
def crear_minas_numeros(matr, x, y):
    for i in range(int(x)):
        for j in range(int(y)):
            if matr[i][j] == 1:
                matr[i][j] = mina(i, j)
            else:
                matr[i][j] = numero(i, j)
    return matr
def table(matr, x, y):
    lista = []
    listaux = []
    for i in range(int(x)):
        for j in range(int(y)):
            if len(listaux) < int(y):
                listaux.append(Casilla(i, j).get_val())
        lista.append(listaux)
        listaux = []
    return lista
def actualizar_y_dibujar_tablero(lista, x, y):
    print((int(x) + 1) * "-+-")
    print("  |",end="")
    for i in range(int(x)):
        print(f" {i + 1}|", end="")
    print("\n" + (int(x) + 1) * "-+-")
    for i in range(int(x)):
        print(f" {i + 1}|", end="")
        for j in range(int(y)):
            if Casilla.get_lev(lista[i][j]) == True:
                if Casilla.get_val(lista[i][j]) == 0:
                    cant_de_minas = numero(i, j).analizar_minas(lista)
                    if cant_de_minas == 0:
                        print("  |", end="")
                    else:
                        print(f" {cant_de_minas}|", end="")
                else:
                    print(" X|", end = "")
            else:
                print(" x|", end="")
        print()        
dim = str(input("Introduzca las dimensiones de tu tablero (filas,columnas): "))
(x, y) = dim.split(",")
matr = Tablero(x, y)
matr = Tablero.crear_tab(matr)
matr = table(matr, x, y)
matr = crear_minas_numeros(matr, x, y)
seguirjugando = True
try:
    while seguirjugando == True:
        jugada = input("Tu jugada(fila,columna): ")
        (x,y) = jugada.split(",")
        if Casilla.get_lev(matr[x][y]) == False:
            if Casilla.get_val(matr[x][y])
        matr = levantar_auto(matr)
        actualizar_y_dibujar_tablero(matr, x, y)
        
        
        
