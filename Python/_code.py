txt = "Un texto para probar a este algoritmo de aqui"

def transform(str):
    sol = ""
    str = str.lower()
    for i in range(0, len(str)):
        if str[i] != " ": sol = sol + str[i]
    print("Sol: %s" % sol)
    return sol

def code(str):
    leng = int(len(str) / 2)
    parejas = {}
    for i in range(0, leng):
        nStr = str[i*2] + str[i*2+1]
        if nStr in parejas:
            parejas[nStr] += 1
        else:
            parejas[nStr] = 1
    return parejas
print (code(transform(txt)))