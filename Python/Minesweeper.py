'''
Created on 24 jul. 2019

@author: asies
'''
import random
import string
import os
or_grid = []
vi_grid = []

def start():
    clearAll()
    print("Filas:")
    rows = int(input())
    print("Columnas:")
    cols = int(input())  
    print("Bombas:")
    bombs = int(input())
    clearAll()
    print("Generando partida de %dx%d con %d bombas..." % (rows, cols, bombs))
    generator(cols, rows, bombs)

def generator (cols, rows, bombs):
    global or_grid
    or_grid = [["0" for i in range(cols)] for j in range(rows)]
    bombs_list = {}
    for e in range(0, bombs):
        while True:
            j = random.randint(0, rows - 1)
            i = random.randint(0, cols - 1)
            if or_grid[j][i] == "0":
                or_grid[j][i] = "B"
                bombs_list[e] = [j, i]
                break
    for b in range(len(bombs_list.keys())):
        j = bombs_list[b][0]
        i = bombs_list[b][1]
        #TL
        if j != 0 and i != 0:
            a = str(or_grid[j-1][i-1])
            if a.isdigit():
                or_grid[j-1][i-1] = int(or_grid[j-1][i-1]) + 1
        #T
        if j != 0:
            a = str(or_grid[j-1][i])
            if a.isdigit():
                or_grid[j-1][i] = int(or_grid[j-1][i]) + 1
        #TR
        if j != 0 and i != cols - 1:
            a = str(or_grid[j-1][i+1])
            if a.isdigit():
                or_grid[j-1][i+1] = int(or_grid[j-1][i+1]) + 1
        #L
        if i != 0:
            a = str(or_grid[j][i-1])
            if a.isdigit():
                or_grid[j][i-1] = int(or_grid[j][i-1]) + 1
        #R
        if i != cols - 1:
            a = str(or_grid[j][i+1])
            if a.isdigit():
                or_grid[j][i+1] = int(or_grid[j][i+1]) + 1
        #BL
        if j != rows - 1 and i != 0:
            a = str(or_grid[j+1][i-1])
            if a.isdigit():
                or_grid[j+1][i-1] = int(or_grid[j+1][i-1]) + 1
        #B
        if j != rows - 1:
            a = str(or_grid[j+1][i])
            if a.isdigit():
                or_grid[j+1][i] = int(or_grid[j+1][i]) + 1
        #BR
        if j != rows - 1 and i != cols - 1:
            a = str(or_grid[j+1][i+1])
            if a.isdigit():
                or_grid[j+1][i+1] = int(or_grid[j+1][i+1]) + 1
    printGrid(or_grid)
    
def printGrid(grid):
    j_l = [i for i in range(1, len(grid) + 1)]
    i_l = list(string.ascii_uppercase)
    if len(grid[0]) > 26:
        for i in range(0, int(len(grid[0]) / 26)):
            for e in range(26):
                i_l.append(i_l[i]+i_l[e])
    print("\\\\\   ", end="")
    for i in range(len(grid[0])):
        if len(i_l[i]) == 1: print(i_l[i]+"   ", end="")
        else: print(i_l[i]+"  ", end="")
    print("\n", end="")
    for j in range(len(grid)):
        print("%02d|" % j_l[j], end="")
        for i in range(len(grid[0])):
            print("   "+str(grid[j][i]), end="")
        print("\n", end="")

def clearAll():
    if os.name == "posix": print("clear")
    else: print("cls")
    
    os.system("cls")

start()