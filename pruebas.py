import unittest
import libvecnmat as lib
import numpy as np

class Testlibvecnmat(unittest.TestCase):

    def test_sumvec(self):
        v = [1-2j, 4-3j, 3-1j]
        w = [3j, 1+2j, 3-2j]
        sum = [(1+1j), (5-1j), (6-3j)]
        suma = lib.sumvec(v,w)
        self.assertEqual(suma,sum)

    def test_invvec(self):
        a = [1+1j, 3-2j, 3j]
        inv = [0j, 0j, 0j]
        inva = lib.invvec(a)
        self.assertEqual(inva,inv)

    def test_multcxvec(self):
        vf = [0+0j, 5+1j, 4]
        c = 3+2j
        mult = [(0+0j), (13+13j), (12+8j)]
        multa = lib.multcxvec(c,vf)
        self.assertEqual(multa,mult)

    def test_summat(self):
        matriz = [[2, 3j], [3, 4j]]
        matriz2 = [[1, 2j], [-1, -1j]]
        sum = [[3, 5j], [2, 3j]]
        suma = lib.summat(matriz,matriz2)
        self.assertEqual(suma,sum)

    def test_invmat(self):
        matriz = [[1j, -3j], [6j, 4j]]
        inv = [[0j, 0j], [0j , 0j]]
        inva = lib.invmat(matriz)
        self.assertEqual(inva,inv)

    def test_multcxmat(self):
        matriz1 = [[1-1j, 2+2j], [3, 4+1j]]
        c1 = 1 + 4j
        mult = [[(5+3j), (-6+10j)], [(3+12j), 17j]]
        multa = lib.multcxmat(c1,matriz1)
        self.assertEqual(multa,mult)

    def test_transp(self):
        matriz3 = [[(1-1j), (7+1j)], [(2-3j), (3+2j)]]
        tran = [[(1-1j), (2-3j)], [(7+1j), (3+2j)]]
        trans = lib.transp(matriz3)
        self.assertEqual(trans,tran)

    def test_conjug(self):
        matriz3 = [[(1-1j), (7+1j)], [(2-3j), (3+2j)]]
        conj = [[(1+1j), (7-1j)], [(2+3j), (3-2j)]]
        conju = lib.conjug(matriz3)
        self.assertEqual(conju,conj)

    def test_dagamat(self):
        matriz3 = [[(1-1j), (7+1j)], [(2-3j), (3+2j)]]
        daga = [[(1+1j), (2+3j)], [(7-1j), (3-2j)]]
        daga1 = lib.dagamat(matriz3)
        self.assertEqual(daga1,daga)

    def test_multmat(self):
        mat1 = [[3 + 2j, 0, 5 - 6j], [1, 4 + 2j, 1j], [4 - 1j, 0, 4]]
        mat2 = [[5, 2 - 1j, 6 - 4j], [0, 4 + 5j, 2], [7 - 4j, 2 + 7j, 0]]
        mult = [[(26-52j), (60+24j), (26+0j)], [(9+7j), (1+29j), (14+0j)], [(48-21j), (15+22j), (20-22j)]]
        mult1 = lib.multmat(mat1,mat2)
        self.assertEqual(mult1,mult)

    def test_accion(self):
        mat = [[1j, 3+2j], [5, -1j]]
        vec = [2,1j]
        acc = [[-2+5j, 11]]
        acc1 = lib.accion(mat,vec)
        self.assertEqual(acc1,acc)

    def test_prodint(self):
        v = [2j, 3 + 5j, 2]
        w = [3j, 2j, 1j]
        prod = (-16+8j)
        prod1 = lib.prodint(v,w)
        self.assertEqual(prod1,prod)

    def test_norma(self):
        vec = [3,-6,2]
        nor = 7
        nor1 = lib.norma(vec)
        self.assertEqual(nor1,nor)

    def test_distancia(self):
        v = [3, 1, 2]
        w = [2, 2, -1]
        dist = np.sqrt(11)
        dist1 = lib.distancia(v,w)
        self.assertEqual(dist1,dist)

    def test_valnvecp(self):
        matriz = [[-1, 1j], [-1j, 1]]
        vnv = (([-1.41421356+0.j,1.41421356+0.j]),([[0.92387953+0.j,-0.+0.38268343j],[-0.+0.38268343j,0.92387953+0.j]]))
        vnv2 = lib.valnvecp(matriz)
        self.assertEqual(vnv2,vnv)

    def test_unitaria(self):
        matriz1 = [[2,2+1j],[-2+1j,2]]
        mat = [[(9+0j), 0j], [0j, (9+0j)]]
        mat1 = lib.unitaria(matriz1)
        self.assertEqual(mat1,mat)

    def test_hermitiana(self):
        matriz = [[5, 4 + 5j, 6 - 16j], [4 - 5j, 13, 7], [6 + 16j, 7, -2]]
        b = True
        resp = lib.hermitiana(matriz)
        self.assertEqual(resp,b)

    def prodtensor(self):
        A = [[2, 3], [1, 4]]
        B = [[5, 3, 2], [1, 0, 2], [-2, 5, 6]]
        resp = [[10, 6, 4, 15, 9, 6], [2, 0, 4, 3, 0, 6], [-4, 10, 12, -6, 15, 18], [5, 3, 2, 20, 12, 8], [1, 0, 2, 4, 0, 8], [-2, 5, 6, -8, 20, 24]]
        resp2 = lib.prodtensor(A,B)
        self.assertEqual(resp2,resp)

if __name__ == '__main__':
    unittest.main()
