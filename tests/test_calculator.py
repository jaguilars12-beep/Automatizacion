import unittest
from src.calculator import  *

class TestCalculator(unittest.TestCase):
    def test_suma(self):
        self.assertAlmostEqual(suma(2, 3), 5)

    def test_resta(self):
        self.assertAlmostEqual(resta(5, 3), 2)

if __name__=='__main__':
    unittest.main()
    