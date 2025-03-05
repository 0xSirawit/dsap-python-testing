import unittest
from src.fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.fizz_cases = [3, 6, 9, 12]
        self.buzz_cases = [5, 10, 20, 25]
        self.fizzbuzz_cases = [15, 30, 45, 60]
        self.number_cases = [1, 2, 4, 7, 8]

    def test_fizzbuzz_divisible_of_3_and_5(self):
        for num in self.fizzbuzz_cases:
            with self.subTest(num=num):
                self.assertEqual(fizzbuzz(num), "FizzBuzz")

    def test_fizzbuzz_divisible_by_3(self):
        for num in self.fizz_cases:
            with self.subTest(num=num):
                self.assertEqual(fizzbuzz(num), "Fizz")

    def test_fizzbuzz_divisible_by_5(self):
        for num in self.buzz_cases:
            with self.subTest(num=num):
                self.assertEqual(fizzbuzz(num), "Buzz")

    def test_fizzbuzz_not_divisible_by_3_or_5(self):
        for num in self.number_cases:
            with self.subTest(num=num):
                self.assertEqual(fizzbuzz(num), str(num))

    def test_fizzbuzz_give_zero(self):
        self.assertEqual(fizzbuzz(0), "FizzBuzz")
