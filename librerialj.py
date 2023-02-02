import math

def sumacplx(c1,c2):
    real = c1[0] + c2[0]
    ima = c1[1] + c2[1]
    resul = (real,ima)
    return resul

def multcplx(c1,c2):
    real = (c1[0]*c2[0]) - (c1[1]*c2[1])
    ima = (c1[0]*c2[1]) + (c2[0]*c1[1])
    resul = (real,ima)
    return resul

def rescplx(c1,c2):
    real = c1[0] - c2[0]
    ima = c1[1] - c2[1]
    resul = (real,ima)
    return resul

def divcplx(c1,c2):
    den = c2[0]**2 + c2[1]**2
    x = c1[0]*c2[0] + c1[1]*c2[1]
    y = c2[0]*c1[1] - c1[0]*c2[1]
    resul = (x/den, y/den)
    return resul

def moducplx(c):
    mod = round(math.sqrt(c[0]**2 + c[1]**2),2)
    return mod

def conjugado(c):
    return (c[0],-c[1])

def polycar(c):
    real = round(c[0]*math.cos(c[1]),2)
    ima = round(c[0]*math.sin(c[1]),2)
    resul = (real, ima)
    return resul

def carypol(c):
    magp = round(math.sqrt(c[0]**2 + c[1]**2),2)
    fase = round(fasecplx(c),2)
    resul = (magp, fase)
    return resul

def fasecplx(c):
    fase = round(math.degrees(math.atan(c[1]/c[0])),2)
    return fase

def prettypcplx(c):
    print("{} + {}i".format(c[0],c[1]))

def prettypol(c):
    print("{} , {}".format(c[0],c[1]))
