import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2),3)
        self.assertEqual(add(5,10),15)
        self.assertEqual(add(-5,10),-15)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(4,2),2)
        self.assertEqual(sub(10,5),5)
        self.assertEqual(sub(30,10),20)
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
        self.assertRaises(ZeroDivisionError, div(0,5))

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(5,125),3)
        self.assertEqual(log(3,81),4)
        self.assertEqual(log(2,32),5)

    def test_log_invalid_base(self): # 1 assertion
        self.assertRaises(ValueError, log(-5,125))
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()