'''
Created on 22 jul. 2019

@author: asies
'''
a, b = 1, 5000

def primo(numero):
    if numero == 1: return False
    for i in range(2, numero):
        if(numero % i) == 0:
            return False
    return numero
for i in range(a, b):
    if(primo(i)):
        print(i)