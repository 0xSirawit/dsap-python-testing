import unittest
from src.funny_string import funnyString


class TestFunnyString(unittest.TestCase):
    def test_funny_string_simple(self):
        # Arrange
        s = "acxz"
        expected = "Funny"

        # Act
        result = funnyString(s)

        # Assert
        self.assertEqual(result, expected, f"Should be '{expected}'")

    def test_not_funny_string_simple(self):
        # Arrange
        s = "bcxz"
        expected = "Not Funny"

        # Act
        result = funnyString(s)

        # Assert
        self.assertEqual(result, expected, f"Should be'{expected}'")

    def test_single_character_string(self):
        # Arrange
        s = "a"
        expected = "Funny"

        # Act
        result = funnyString(s)

        # Assert
        self.assertEqual(
            result, expected, f"Single character string should be '{expected}'"
        )

    def test_two_character_string(self):
        # Arrange
        s = "ab"
        expected = "Funny"

        # Act
        result = funnyString(s)

        # Assert
        self.assertEqual(
            result, expected, f"Two character string should be '{expected}'"
        )

    def test_palindrome_string(self):
        # Arrange
        s = "racecar"
        expected = "Funny"

        # Act
        result = funnyString(s)

        # Assert
        self.assertEqual(result, expected, f"Palindrome string should be '{expected}'")
