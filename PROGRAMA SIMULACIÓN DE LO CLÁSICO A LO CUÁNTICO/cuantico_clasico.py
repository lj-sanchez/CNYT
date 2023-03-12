import libvecnmat as lib
import librerialj as lj
import numpy
import matplotlib.pyplot as pyplot

#Canicas con coeficiente booleanos
def canicas(mat, vec, clic):
    r = lib.multmat(mat, mat)
    clic -= 1
    while clic > 0:
        r = lib.multmat(r, mat)
        clic -= 1
    resul = lib.multmat(r, vec)
    return resul

#Múltiples rendijas clásico probabilístico
def rendija(mat, clic):
    k = 0
    mat1 = mat[:]
    while k != clic:
        for k in range(clic):
            mat = mat1
            k += 1
    fila = len(mat)
    columna = len(mat[0])
    for i in range(fila):
        new_fila = []
        for j in range(columna):
            new_fila.append((lj.moducplx(mat[i][j]))**2)
            mat[i] = new_fila
    return mat

#Múltiples rendijas cuántico
def sist_prob(mat, vec, clic):
    r = lib.multmat(mat, mat)
    clic -= 1
    while clic > 0:
        r = lib.multmat(r, mat)
        clic -= 1
    resul = lib.multmat(r,vec)
    return resul

#Gráfico
def grafico(vec):
    data = len(vec)
    x = numpy.array([x for x in range(data)])
    y = numpy.array([round(vec[x] * 100, 2) for x in range(data)])

    pyplot.bar(x, y, color='r', align='center')
    pyplot.title('Probabilidad del Vector')
    pyplot.show()

if __name__ == '__main__':
    vec = [4/9,4/9,1/9]
    vec = [0,1/3,2/3]
    print(grafico(vec))
