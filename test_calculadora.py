import unittest
import calculadora as calc

# os nomes deverá iniciar sempre com Test
class TestSoma(unittest.TestCase):
    def test_soma(self):
        esperado = 5
        real = calc.somar(3, 2)
        self.assertEqual(esperado, real)

class TestSubtrai(unittest.TestCase):
    def test_subtrai(self):
        esperado = 5
        real = calc.subtrair(7, 2)
        self.assertEqual(esperado, real)

class TestMultiplica(unittest.TestCase):
    def test_multiplica(self):
        esperado = 6
        real = calc.multiplicar(3, 2)
        self.assertEqual(esperado, real)

class TestDividi(unittest.TestCase):
    def test_dividi(self):
        esperado = 5
        real = calc.dividir(10, 2)
        self.assertEqual(esperado, real)

if __name__ == '__main__':
    unittest.main