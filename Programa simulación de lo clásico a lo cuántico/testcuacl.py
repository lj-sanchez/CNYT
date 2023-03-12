import unittest
import cuantico_clasico as cc
import math

class Testcuantico_clasico(unittest.TestCase):

    def test_canicas(self):
        #prueba1
        mat = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0],
               [1, 0, 0, 0, 1, 0]]
        vec = [5, 5, 0, 2, 0, 15]
        clic = 1
        resul = [0,0,20,2,0,5]
        #prueba2
        mat = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0],
               [1, 0, 0, 0, 1, 0]]
        vec = [6, 2, 1, 5, 3, 10]
        clic = 1
        resul = [0, 0, 12, 5, 1, 9]
        #
        aa1 = cc.canicas(mat, vec, clic)
        self.assertEqual(aa1,resul)

    def test_rendija(self):
        #prueba1
        mat = [[0, 2 / 3, 1 / 3], [1 / 3, 0, 2 / 3], [2 / 3, 1 / 3, 0]]
        clic = 2
        mat = [4 / 9, 4 / 9, 1 / 9]
        #prueba2
        mat = [[0, 2 / 3, 1 / 3], [1 / 3, 0, 2 / 3], [2 / 3, 1 / 3, 0]]
        clic = 1
        mat = [0,1/3,2/3]
        #
        mat1 = cc.rendija(mat, clic)
        self.assertEqual(mat1, mat)

    def test_sist_prob(self):
        #prueba1
        mat = [[1 / math.sqrt(2), -1j / math.sqrt(2), 0], [1 / math.sqrt(2), 1j / math.sqrt(2), 0], [0, 0, 1j]]
        vec = [1, 0, 0]
        clic = 1
        resul = [1/math.sqrt(2),-1j/math.sqrt(2),0]
        #prueba2
        mat = [[1 / math.sqrt(2), -1j / math.sqrt(2), 0], [1 / math.sqrt(2), 1j / math.sqrt(2), 0], [0, 0, 1j]]
        vec = [0, 0, 1]
        clic = 1
        resul = [0,0,1j]
        #
        bb1 = cc.sist_prob(mat, vec, clic)
        self.assertEqual(bb1,resul)

if __name__ == '__main__':
    unittest.main()
