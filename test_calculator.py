#Github link: https://github.com/fanggs/lab11-HS-AT.git
#Partner 1: Hector Salvatierra
#Partner 2: Alan Tran

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(5, 4), 9)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(2, 2), 0)
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(4, 2), 2)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(7,3), 21)
        self.assertEqual(multiply(4,-2), -8)
        self.assertEqual(multiply(-1, 0.1), -0.1)

    def test_divide(self): # 3 assertions
        self.assertEqual(divide(16, 4), 4)
        self.assertEqual(divide(-4, 2), -2)
        self.assertAlmostEqual(divide(10, 3), 3.33, 2)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
       with self.assertRaises(ZeroDivisionError):
           divide(5, 0)
            

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 8), 3)
        self.assertEqual(logarithm(10, 100), 2)
        self.assertEqual(logarithm(5, 1), 0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-2, 8)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)


    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertEqual(hypotenuse(-3, 4), 5)
        self.assertAlmostEqual(hypotenuse(4, 2), 4.47, 2)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        with self.assertRaises(ValueError):
           square_root(-4)
        self.assertEqual(square_root(16), 4)
        self.assertAlmostEqual(square_root(20), 4.47, 2)
       
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()