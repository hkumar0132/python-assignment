import unittest
from main import Solution
from config import PRODUCT_DOES_NOT_EXIST_ERROR_MESSAGE


class TestReturnMaximumTotalSales(unittest.TestCase):
    test_solution = Solution()

    def test_product_name_does_not_exist(self):
        product_name = 'XYZ'
        expected = PRODUCT_DOES_NOT_EXIST_ERROR_MESSAGE
        actual = self.test_solution._return_maximum_total_sales(product_name)
        self.assertEqual(actual, expected)

    def test_product_name_is_none(self):
        product_name = None
        expected = PRODUCT_DOES_NOT_EXIST_ERROR_MESSAGE
        actual = self.test_solution._return_maximum_total_sales(product_name)
        self.assertEqual(actual, expected)

    def test_product_name_is_A(self):
        product_name = 'A'
        expected = 'Germany'
        actual = self.test_solution._return_maximum_total_sales(product_name)
        self.assertEqual(actual, expected)

    def test_product_name_is_B(self):
        product_name = 'B'
        expected = 'Germany'
        actual = self.test_solution._return_maximum_total_sales(product_name)
        self.assertEqual(actual, expected)

    def test_product_name_is_C(self):
        product_name = 'C'
        expected = 'Germany'
        actual = self.test_solution._return_maximum_total_sales(product_name)
        self.assertEqual(actual, expected)

    def test_product_name_is_D(self):
        product_name = 'D'
        expected = 'France'
        actual = self.test_solution._return_maximum_total_sales(product_name)
        self.assertEqual(actual, expected)

    def test_product_name_is_E(self):
        product_name = 'E'
        expected = 'USA'
        actual = self.test_solution._return_maximum_total_sales(product_name)
        self.assertEqual(actual, expected)
