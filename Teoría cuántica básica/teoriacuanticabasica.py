import libvecnmat as lib
import numpy as np

#Norma del vector
def norm(ket):
    ket = round((np.linalg.norm(ket))**2,3)
    return ket

#Probabilidad
def prob(ket,posicion):
    pos = ket[posicion]
    return round(np.abs(pos)**2 / norm(ket),3)

#Probabilidad de transitar
def probt(ket,ket2):
    return np.abs(np.dot(ket2.conj(),ket))**2

#Amplitud de transición
def amptran(vec,vec2):
    return np.round(np.dot(vec2.conj(),vec),2)

#Valor esperado es la media/promedio
def media(matriz,ket): #matriz->observable, vector->ket
    if lib.hermitiana(matriz):
        var = lib.accion(matriz, ket)
        var2 = lib.prodint(var, ket)
        return var2
    else:
        return "No se puede resolver, la matriz no es hermitiana"

#Varianza (Uso del Operador delta)
def varianza(matriz,ket,matrizI):
    if lib.hermitiana(matriz):
        media1 = media(matriz,ket)
        var = lib.multcxmat(media1,matrizI)
        var2 = lib.invmat(var)
        opdelta = lib.summat(matriz,var2)
        varianza1 = lib.multmat(opdelta,opdelta)
        return varianza1
    else:
        return "No se puede resolver, la matriz no es hermitiana"

#Valores propios del observable
def valprop(matriz):
    val = np.linalg.eigvals(matriz)
    return val

#Probabilidad de que el sistema transite a alguno de los vectores propios después de la observación
def probab(matriz,vec):
    resp = lib.accion(matriz,vec)
    return resp

def dinamica(matriz,matriz2):
    resp = lib.multmat(matriz,matriz2)
    return resp

#Ejercicio 4.3.1
def ejer1():
    v = [[1, 0], [0, 0]]
    m = [[(0, 0), (1, 0)], [(1, 0), (0, 0)]]
    vecresul = lib.accion(m,v)
    val = np.linalg.eigvals(m)
    vec = np.linalg.eig(m)
    print("El resultado de la observación es" , vecresul)
    print("Valores propios ", val, "Vectores propios ", vec)

#Ejercicio 4.3.2
def ejer2():
    v = [[1,0],[0,0]]
    m = [[(0,0),(1,0)],[(1,0),(0,0)]]
    val = np.linalg.eigvals(m)
    vec = np.linalg.eig(m)
    for i in range(len(vec)):
        print(amptran(v,vec[i]))

#Ejercicio 4.4.1
def ejerc1():
    u = [[(0,0),(1,0)],[(1,0),(0,0)]]
    u2 = [[(np.sqrt(2)/2,0),(np.sqrt(2)/2,0)],[(np.sqrt(2)/2,0),(np.sqrt(2)/(-2),0)]]
    if lib.unitaria(u) and lib.unitaria(u2):
        print(lib.multmat(u,u2))

#Ejercicio 4.4.2
def ejerc2:
    m = [[0,1/np.sqrt(2),1/np.sqrt(2),0],[1j/np.sqrt(2),0,0,1/np.sqrt(2)],[1/np.sqrt(2),0,0,1j/np.sqrt(2)],[0,1/np.sqrt(2),-1/np.sqrt(2),0]]
    vest = [1,0,0,0]
    clic = 3
    if lib.unitaria(m):
        for i in range(clic):
            vest = lib.accion(m,vest)
            print(vest)
        else:
            print("No se puede resolver, la matriz no es unitaria")

ejer1();
print()
ejer2();
print()
ejerc1();
print()
ejerc2();
print()
