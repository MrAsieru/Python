'''
Created on 22 jul. 2019

@author: asies
'''
txt = "Bond, James Bond"
def find(str, x):
    str = str.lower()
    x = x.lower()
    scor = 0
    tcor = 0
    for i in range(0, len(str)):
        if str[i] == x[scor]:
            scor += 1
            if scor == len(x):
                scor = 0
                tcor += 1
    return tcor
print(find(txt, "bond"))