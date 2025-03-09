import unittest
from src.two_chars import twoChars


class TestTwoChars(unittest.TestCase):
    def test_simple_case(self):
        # Arrange
        s = "abaacdabd"
        expected = 4

        # Act
        result = twoChars(s)

        # Assert
        self.assertEqual(result, expected, f"Should return {expected} for string '{s}'")

    def test_no_alter(self):
        # Arrange
        s = "aaa"
        expected = 0

        # Act
        result = twoChars(s)

        # Assert
        self.assertEqual(
            result,
            expected,
            f"Should return {expected} when no alter string is possible",
        )

    def test_empty_string(self):
        # Arrange
        s = ""
        expected = 0

        # Act
        result = twoChars(s)

        # Assert
        self.assertEqual(result, expected, f"Should return {expected} for empty")

    def test_two_character_string(self):
        # Arrange
        s = "ab"
        expected = 2

        # Act
        result = twoChars(s)

        # Assert
        self.assertEqual(
            result,
            expected,
            f"Should return {expected} for already alter string '{s}'",
        )

    def test_multiple_options(self):
        # Arrange
        s = "beabeefeab"
        expected = 5

        # Act
        result = twoChars(s)

        # Assert
        self.assertEqual(
            result,
            expected,
            f"Should return {expected} for string with multiple options '{s}'",
        )

    def test_single_character_string(self):
        # Arrange
        s = "x"
        expected = 0

        # Act
        result = twoChars(s)

        # Assert
        self.assertEqual(result, expected, f"Should return {expected} for single char")
