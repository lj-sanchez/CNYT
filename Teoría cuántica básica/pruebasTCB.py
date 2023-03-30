import unittest
import teoriacuanticabasica as tcb
import numpy as np

class Testteoriacuanticabasica(unittest.TestCase):

    def test_prob(self):
        ket = [2 - 1j, 2j, 1 - 1j, 1, -2j, 2]
        posicion = 3
        resp = 0.05
        resp1 = tcb.prob(ket,posicion)
        self.assertEqual(resp1,resp)

    def test_probt(self):
        ket = np.array([1 + 1j, 1j])
        ket2 = np.array([2 + 4j, -1 + 3j])
        resp = 90
        resp1 = tcb.probt(ket,ket2)
        self.assertEqual(resp1,resp)

    def test_amptran(self):
        vec = np.array([np.sqrt(2)/2j, np.sqrt(2)/(-2)])
        vec2 = np.array([np.sqrt(2)/2, np.sqrt(2)/2j])
        resp = -1j
        resp1 = tcb.amptran(vec,vec2)
        self.assertEqual(resp1,resp)

    def test_media(self):
        matriz = [[3, 1 + 2j], [1 - 2j, -1]]
        ket = [np.sqrt(2) / 2, np.sqrt(2) / (-2)]
        resp = 0+0j
        resp1 = tcb.media(matriz,ket)
        self.assertEqual(resp1,resp)

    def test_varianza(self):
        matriz = [[3, 1 + 2j], [1 - 2j, -1]]
        ket = [np.sqrt(2) / 2, np.sqrt(2) / (-2)]
        matrizI = [[1, 0], [0, 1]]
        resp = [[14+0j,2+4j],[2-4j,6+0j]]
        resp1 = tcb.varianza(matriz,ket,matrizI)
        self.assertEqual(resp1, resp)

    def test_valprop(self):
        matriz = [[1, 0], [0, -1]]
        resp = [1,-1]
        resp1 = tcb.valprop(matriz)
        self.assertEqual(resp1, resp)

    def test_probab(self):
        matriz = [[0, 1], [1, 0]]
        vec = [1, 0]
        resp = [0,1]
        resp1 = tcb.probab(matriz,vec)
        self.assertEqual(resp1, resp)

    def test_dinamica(self):
        matriz = [[0, 1], [1, 0]]
        matriz2 = [[np.sqrt(2) / 2, np.sqrt(2) / 2], [np.sqrt(2) / 2, np.sqrt(2) / (-2)]]
        resp = [[np.sqrt(2)/2, np.sqrt(2)/(-2)],[np.sqrt(2)/2, np.sqrt(2)/2]]
        resp1 = tcb.dinamica(matriz,matriz2)
        self.assertEqual(resp1, resp)

if __name__ == '__main__':
    unittest.main()
