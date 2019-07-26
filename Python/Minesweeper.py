'''
Created on 24 jul. 2019
@author: MrAsieru
'''
import random
import string
import os
import time

rows = None
cols = None
bombs = None
or_grid = []
vi_grid = []
j_l = []
i_l = []
cleared = {}
mark_bombs = 0
startTime = 0
gameOver = False

def start():
    global rows, cols, bombs, vi_grid
    clearAll()
    print("Filas:")
    while True:
        try:
            rows = int(input())
            break
        except:
            print("Inserte un numero")
            print("Filas:")
    print("Columnas:")
    while True:
        try:
            cols = int(input())
            break
        except:
            print("Inserte un numero")
            print("Columnas:")
    print("Bombas:")
    while True:
        try:
            bombs = int(input())
            break
        except:
            print("Inserte un numero")
            print("Bombas:")
    clearAll()
    print("Generando partida de %dx%d con %d bombas..." % (rows, cols, bombs))
    generator()
    vi_grid = [["#" for i in range(cols)] for j in range(rows)]
    print("")
    inputManager()

def generator ():
    global or_grid, rows, cols, bombs, mark_bombs
    or_grid = [["0" for i in range(cols)] for j in range(rows)]
    bombs_list = {}
    mark_bombs = bombs
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
    
def printGrid(grid):
    global j_l, i_l
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

def inputManager():
    global or_grid, vi_grid, j_l, i_l, startTime, mark_bombs, rows, cols, bombs
    startTime = time.time()
    while len(cleared.keys()) != (rows*cols) - bombs:
        print("%d != %d: %s" %(len(cleared.keys()), rows*cols - bombs, len(cleared.keys()) != (rows*cols) - bombs))
        printGrid(or_grid)
        printGrid(vi_grid)
        print("Tiempo: %dh %dm %ds" % (getTiempo()[0], getTiempo()[1], getTiempo()[2]))
        print("Quedan %d bombas" % mark_bombs)
        print("")
        print("Insertar letra y numero de casilla para despejar. Ej. A01")
        print("Insertar 'mark' mas letra y numero de casilla para marcar y desmarcar. Ej. mark A01")
        inp = input()
        inp = inp.upper()
        clearAll()
        try:
            if inp[:4] == "MARK":
                inp = inp[5:]
                inp_l = inp[:len(inp)-2]
                inp_n = int(inp[len(inp)-2:])
                for i in range(len(i_l)):
                    if i_l[i] == inp_l:
                        inp_l = i
                for j in range(len(j_l)):
                    if j_l[j] == inp_n:
                        inp_n = j
                marcarCasilla(int(inp_n), int(inp_l))
            else:
                inp_l = inp[:len(inp)-2]
                inp_n = int(inp[len(inp)-2:])
                for i in range(len(i_l)):
                    if i_l[i] == inp_l:
                        inp_l = i
                for j in range(len(j_l)):
                    if j_l[j] == inp_n:
                        inp_n = j
                if or_grid[inp_n][inp_l] == "0":
                    desbloquearCeros(int(inp_n), int(inp_l))
                    desbloquearAlrededorCeros()
                elif or_grid[inp_n][inp_l] == "B":
                    perdido()
                    break
                elif vi_grid[inp_n][inp_l] == "#":
                    desbloquear(int(inp_n), int(inp_l))
        except:
            pass
    if not gameOver:
        printGrid(or_grid)
        print("Has ganado! En %dh %dm %ds" % (getTiempo()[0], getTiempo()[1], getTiempo()[2]))

def desbloquear(j, i):
    cleared[len(cleared.keys())] = [j, i]
    vi_grid[j][i] = or_grid[j][i]

def desbloquearCeros(j, i):
    for e in cleared.values():
        if j == e[0] and i == e[1]:
            return
    if or_grid[j][i] == "0":
        vi_grid[j][i] = "0"
        cleared[len(cleared.keys())] = [j, i]
    else:
        return
    #T
    if j != 0:
        desbloquearCeros(j-1, i)
    #L
    if i != 0:
        desbloquearCeros(j, i-1)
    #R
    if i != cols - 1:
        desbloquearCeros(j, i+1)
    #B
    if j != rows - 1:
        desbloquearCeros(j+1, i)

def desbloquearAlrededorCeros():
    global or_grid, vi_grid, cleared
    for a in range(len(vi_grid)):
        for b in range(len(vi_grid[0])):
            if or_grid[a][b] == "0" and [a, b] in cleared.values():
                #T
                if a!= 0:
                    if b!= 0:
                        vi_grid[a-1][b-1] = or_grid[a-1][b-1]
                        cleared[len(cleared.keys())] = [j-1, i-1]
                    vi_grid[a-1][b] = or_grid[a-1][b]
                    cleared[len(cleared.keys())] = [j-1, i]
                    if b != rows - 1:
                        vi_grid[a-1][b+1] = or_grid[a-1][b+1]
                        cleared[len(cleared.keys())] = [j-1, i+1]
                #C
                if b!= 0:
                        vi_grid[a][b-1] = or_grid[a][b-1]
                        cleared[len(cleared.keys())] = [j, i-1]
                if b != cols - 1:
                        vi_grid[a][b+1] = or_grid[a][b+1]
                        cleared[len(cleared.keys())] = [j, i+1]
                #B
                if a != rows - 1:
                    if b != 0:
                        vi_grid[a+1][b-1] = or_grid[a+1][b-1]
                        cleared[len(cleared.keys())] = [j+1, i-1]
                    vi_grid[a+1][b] = or_grid[a+1][b]
                    cleared[len(cleared.keys())] = [j+1, i]
                    if b != cols - 1:
                        vi_grid[a+1][b+1] = or_grid[a+1][b+1]
                        cleared[len(cleared.keys())] = [j+1, i+1]
                
def marcarCasilla(j, i):
    global mark_bombs
    if vi_grid[j][i] == "#":
        vi_grid[j][i] = "@"
        mark_bombs -= 1
    elif vi_grid[j][i] == "@":
        vi_grid[j][i] == "#"
        mark_bombs += 1


def perdido():
    global gameOver, or_grid
    gameOver = True
    printGrid(or_grid)
    print("")
    print("  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  ")
    print(" ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒")
    print("▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒")
    print("░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  ")
    print("░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒")
    print(" ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░")
    print("  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░")
    print("░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ ")
    print("      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     ")
    print("                                                     ░                   ")
    
    
def getTiempo():
    global startTime
    timeDelta = time.time() - startTime
    return [int(timeDelta / 3600), int(timeDelta / 60), int(timeDelta)]

def clearAll():
    if os.name == "posix": print("clear")
    else: print("cls")
    
    os.system("cls")

start()
