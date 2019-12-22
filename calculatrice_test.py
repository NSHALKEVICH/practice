import unittest
import calculatrice

class CalculatriceTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculatrice.add(2, 5), 7)

    def test_sub(self):
        self.assertEqual(calculatrice.sub(5, 2), 3)

    def test_mul(self):
        self.assertEqual(calculatrice.mul(2, 5), 10)

    def test_div(self):
        self.assertEqual(calculatrice.div(5, 5), 1)

    def test_power(self):
        self.assertEqual(calculatrice.power(2, 3), 8)

    def test_root(self):
        self.assertEqual(calculatrice.root(8, 3), 2)
        
if __name__ == '__main__':
    unittest.main()