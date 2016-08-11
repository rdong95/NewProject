#!/usr/bin/python

import unittest
from calculator import Calculator

class TddInPythonExample(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)

    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')
    
    def test_calculator_subtract_method_returns_correct_result(self):
	result = self.calc.subtract(4,2)
	self.assertEqual(2, result)
    
    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
	self.assertRaises(ValueError, self.calc.subtract, "four", "two")
    def test_calculator_multiply_method_returns_correct_result(self):
	result = self.calc.multiply(3,5)
	self.assertEqual(15, result)
    def test_calculator_returns_error_message_if_both_args_not_number(self):
	self.assertRaises(ValueError, self.calc.multiply, "three","five")
    def test_calculator_divide_method_returns_correct_result(self):
	result = self.calc.divide(15,3)
	self.assertEqual(5, result)
    def test_calcualtor_returns_error_message_if_btoh_args_not_number(self):
	self.assertRaises(ValueError, self.calc.divide, "fifteen","three")

if __name__ == '__main__':
    unittest.main()
