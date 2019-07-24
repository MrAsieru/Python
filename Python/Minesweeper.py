'''
Created on 24 jul. 2019

@author: asies
'''
import random
def generator (cols, rows, bombs):
    grid = [["#" for i in range(cols)] for j in range(rows)]
    bombs_list = {}
    for e in range(0, bombs):
        while True:
            i = random.randint(0, rows - 1)
            j = random.randint(0, cols - 1)
            if grid[i][j] == "#":
                grid[i][j] = "B"
                bombs_list[e] = [i, j]
                break
    for b in range(len(bombs_list.keys())):
        i = bombs_list[b][0]
        j = bombs_list[b][1]
        #top
        
    
    print(grid)
    print (len(grid[0]))
    
def printGrid(grid):
    print (len(grid))
    
generator(2, 10, 20)

