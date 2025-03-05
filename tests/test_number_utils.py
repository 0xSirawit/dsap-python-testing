import unittest
from src.number_utils import is_prime_list


class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_not_prime(self):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_2_3_5_is_prime(self):
        prime_list = [2, 3, 5]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_13_17_19_is_prime(self):
        prime_list = [13, 17, 19]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_1_2_4_5_7_is_mixed(self):
        prime_list = [1, 2, 4, 5, 7]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_9_is_not_prime(self):
        prime_list = [9]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_2_is_prime(self):
        prime_list = [2]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_empty(self):
        prime_list = []
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
