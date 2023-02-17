import cmath
import numpy as np

#Suma de vectores
def sumvec(v,w):
    tamanio = len(v)
    suma = [0 + 0j for i in range(tamanio)]
    k = 0
    while k < tamanio:
        suma[k] = v[k] + w[k]
        k = k + 1
    return suma

#Inverso aditivo de un vector
def invvec(a):
    tamanio = len(a)
    inv = [0 + 0j for i in range(tamanio)]
    k = 0
    while k < tamanio:
        inv[k] = a[k] - a[k]
        k = k + 1
    return inv

#Multiplicación de un escalar por un vector
def multcxvec(c,vf):
    tamanio = len(vf)
    mult = [0 + 0j for i in range(tamanio)]
    k = 0
    while k < tamanio:
        mult[k] = c * vf[k]
        k = k + 1
    return mult

#Suma de matrices
def summat(matriz,matriz2):
    sum = []
    for i in range(len(matriz)):
        sum.append([0]*len(matriz))
        for j in range(len(matriz)):
            sum[i][j] = matriz[i][j] + matriz2[i][j]
    return sum

#Inversa aditiva de una matriz
def invmat(matriz):
    mat = []
    for i in range(len(matriz)):
        mat.append([0]*len(matriz))
        for j in range(len(matriz)):
            mat[i][j] = matriz[i][j] - matriz[i][j]
    return mat

#Multiplicación de un escalar por una matriz
def multcxmat(c1,matriz1):
    mult = []
    for i in range(len(matriz1)):
        mult.append([0]*len(matriz1))
        for j in range(len(matriz1)):
            mult[i][j] = matriz1[i][j] * c1
    return mult

#Transpuesta de una matriz
def transp(matriz3):
    mat = []
    for i in range(len(matriz3)):
        mat.append([0]*len(matriz3))
        for j in range(len(matriz3)):
            mat[i][j] = matriz3[j][i]
    return mat

#Conjugada de una matriz
def conjug(matriz3):
    mat = []
    for i in range(len(matriz3)):
        mat.append([0]*len(matriz3))
        for j in range(len(matriz3)):
            mat[i][j] = complex(matriz3[i][j].real,-matriz3[i][j].imag)
    return mat

#Adjunta/daga de una matriz
def dagamat(matriz3):
    mat = []
    return transp(conjug(matriz3))

#Multiplicación de dos matrices
def multmat(mat1,mat2):
    mult = []
    for i in range(len(mat1)):
        mult.append([0] * len(mat2[0]))
        for j in range(len(mat2)):
            for k in range(len(mat2[0])):
                mult[i][j] = mult[i][j] + (mat1[i][k] * mat2[k][j])
    return mult

#Acción de una matriz sobre un vector
def accion(mat,vec):
    acc = []
    for i in range(len(mat)):
        acc.append([0] * len(vec))
        for j in range(len(vec)):
            for k in range(len(vec)):
                acc[i][j] = acc[i][j] + mat[i][k] * vec[k]
    return acc

#Producto interno de dos vectores
def prodint(v,w):
   prod = np.dot(v,w)
   return prod

#Norma de un vector
def norma(vec):
    prod = np.dot(vec,vec)
    nor = np.sqrt(prod)
    return nor

#Distancia entre dos vectores
def distancia(v,w):
    tamanio = len(v)
    res = [0 + 0j for i in range(tamanio)]
    k = 0
    while k < tamanio:
        res[k] = v[k] - w[k]
        k = k + 1
    A = np.dot(res,res)
    dist = np.sqrt(A)
    return dist

#Valores propios de una matriz
def valnvecp(matriz):
    vnv = np.linalg.eig(matriz)
    return vnv

#Revisar si una matriz es unitaria
def unitaria(matriz1):
    mat = []
    a = matriz1
    b = dagamat(matriz1)
    mat = multmat(a,b)
    return mat

#Revisar si una matriz es hermitiana
def hermitiana(matriz):
    a = matriz
    b = dagamat(matriz)
    if a != b:
        return False
    else:
        return True

#Producto tensor de dos matrices
def prodtensor(A,B):
    resp = []
    m = len(A)
    n = len(B)
    m1 = len(A[0])
    n1 = len(B[0])
    nfilas = m*n
    ncolumnas = m1*n1
    for j in range(nfilas):
        resp.append([0]*ncolumnas)
        for k in range(ncolumnas):
            resp[j][k] = A[j//n][k//n1] * B[j%n][k%n1]
    return resp
