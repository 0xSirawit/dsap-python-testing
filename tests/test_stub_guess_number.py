import unittest
from unittest.mock import patch
from src.guess_number import guess_int, guess_float


class TestGuessNumbers(unittest.TestCase):
    # Basic test for guess_int
    @patch("src.guess_number.random.randint")
    def test_basic_guess_int(self, mock_randint):
        mock_randint.return_value = 7
        result = guess_int(1, 10)
        self.assertEqual(result, 7)
        mock_randint.assert_called_with(1, 10)

    # Testing guess_int with same start and stop
    @patch("src.guess_number.random.randint")
    def test_guess_int_same_numbers(self, mock_randint):
        mock_randint.return_value = 5
        result = guess_int(5, 5)
        self.assertEqual(result, 5)
        mock_randint.assert_called_with(5, 5)

    # Basic test for guess_float
    @patch("src.guess_number.random.uniform")
    def test_basic_guess_float(self, mock_uniform):
        mock_uniform.return_value = 3.5
        result = guess_float(1.0, 10.0)
        self.assertEqual(result, 3.5)
        mock_uniform.assert_called_with(1.0, 10.0)

    # Testing guess_float with negative number
    @patch("src.guess_number.random.uniform")
    def test_guess_float_negative(self, mock_uniform):
        mock_uniform.return_value = -7.5
        result = guess_float(-10.0, -5.0)
        self.assertEqual(result, -7.5)
        mock_uniform.assert_called_with(-10.0, -5.0)

    # Testing with zero value
    @patch("src.guess_number.random.randint")
    def test_guess_int_zero_value(self, mock_randint):
        mock_randint.return_value = 0
        result = guess_int(-5, 5)
        self.assertEqual(result, 0)
        mock_randint.assert_called_once_with(-5, 5)

    # Stub test for guess_int
    @patch("src.guess_number.random.randint")
    def test_guess_int_stub(self, mock_randint):
        mock_randint.return_value = 42
        result = guess_int(0, 100)
        self.assertEqual(result, 42)

    # Stub test for guess_float
    @patch("src.guess_number.random.uniform")
    def test_guess_float_stub(self, mock_uniform):
        mock_uniform.return_value = 6.28
        result = guess_float(0.0, 10.0)
        self.assertEqual(result, 6.28)

    # Stub test for guess_int with large numbers
    @patch("src.guess_number.random.randint")
    def test_guess_int_large_numbers_stub(self, mock_randint):
        mock_randint.return_value = 1000000
        result = guess_int(1000, 2000000)
        self.assertEqual(result, 1000000)
