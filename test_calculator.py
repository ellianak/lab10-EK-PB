# https://github.com/ellianak/lab10-EK-PB.git
# Elliana Kirby
# Parker Brock

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2),3)
        self.assertEqual(add(5,10),15)
        self.assertEqual(add(-5,10), 5)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(4,2),2)
        self.assertEqual(subtract(10,5),5)
        self.assertEqual(subtract(30,10),20)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertTrue(mul(2, 2))
        self.assertTrue(mul(-3, 4))
        self.assertTrue(mul(-5, -7))

    def test_divide(self): # 3 assertions
        self.assertTrue(div(2, 3))
        self.assertTrue(div(-4, -5))
        self.assertTrue(div(5, -4))
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
        self.assertRaises(ZeroDivisionError, div(0,5))

    def test_logarithm(self): # 3 assertions
        # self.assertEqual(logarithm(256,2),8)
        # self.assertEqual(logarithm(81,3),4)
        # self.assertEqual(logarithm(32,2),5)
        self.assertFalse(logarithm(2, 2))
        self.assertFalse(logarithm(2, 3))
        self.assertFalse(logarithm(2, 4))

    def test_log_invalid_base(self): # 1 assertion
        self.assertRaises(ValueError, logarithm(-5,125))
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        self.assertRaises(ValueError, logarithm(4, 0))

    def test_hypotenuse(self): # 3 assertions
        self.assertTrue(hypotenuse(2, 2))
        self.assertTrue(hypotenuse(-3, 4))
        self.assertTrue(hypotenuse(-5, -7))

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        self.assertRaises(ValueError, square_root(-4))
        # Test basic function
        self.assertTrue(square_root(2))
        self.assertTrue(square_root(4))
        self.assertTrue(square_root(99))
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()