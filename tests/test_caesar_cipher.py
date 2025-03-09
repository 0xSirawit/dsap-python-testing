import unittest
from src.caesar_cipher import caesarCipher


class TestCaesarCipher(unittest.TestCase):
    def test_basic_encryption_lowercase(self):
        # Arrange
        text = "hello"
        shift = 3
        expected = "khoor"

        # Act
        result = caesarCipher(text, shift)

        # Assert
        self.assertEqual(
            result,
            expected,
            f"Lowercase shift by {shift} should return '{expected}'",
        )

    def test_basic_encryption_uppercase(self):
        # Arrange
        text = "HELLO"
        shift = 3
        expected = "KHOOR"

        # Act
        result = caesarCipher(text, shift)

        # Assert
        self.assertEqual(
            result,
            expected,
            f"Uppercase shift by {shift} should return '{expected}'",
        )

    def test_mixed_case_with_symbols(self):
        # Arrange
        text = "Hello, World!"
        shift = 5
        expected = "Mjqqt, Btwqi!"

        # Act
        result = caesarCipher(text, shift)

        # Assert
        self.assertEqual(
            result, expected, f"Mixed case with symbol should return '{expected}'"
        )

    def test_large_shift(self):
        # Arrange
        text = "abc"
        shift = 30  # Should be equivalent to shift of 4 (30 % 26 = 4)
        expected = "efg"

        # Act
        result = caesarCipher(text, shift)

        # Assert
        self.assertEqual(result, expected, f"Large shift of {shift}")

    def test_zero_shift(self):
        # Arrange
        text = "NoChange"
        shift = 0
        expected = "NoChange"

        # Act
        result = caesarCipher(text, shift)

        # Assert
        self.assertEqual(result, expected, f"Zero shift should return original text")

    def test_negative_shift(self):
        # Arrange
        text = "abc"
        shift = -1  # Should shift backwards
        expected = "zab"

        # Act
        result = caesarCipher(text, shift)

        # Assert
        self.assertEqual(result, expected, f"Negative shift of {shift}")

    def test_empty_string(self):
        # Arrange
        text = ""
        shift = 5
        expected = ""

        # Act
        result = caesarCipher(text, shift)

        # Assert
        self.assertEqual(result, expected, f"Empty should return empty")
