import unittest
from src.alter_char import alternatingCharacters


class TestAlternatingCharacters(unittest.TestCase):
    def test_all_same_characters(self):
        # Arrange
        s = "AAAA"
        expected = 3

        # Act
        result = alternatingCharacters(s)

        # Assert
        self.assertEqual(
            result, expected, f"For string '{s}', should return {expected} deletions"
        )

    def test_perfect_alternating_characters(self):
        # Arrange
        s = "ABABABAB"
        expected = 0

        # Act
        result = alternatingCharacters(s)

        # Assert
        self.assertEqual(
            result,
            expected,
            f"For perfectly alternating string '{s}', should return {expected} deletions",
        )

    def test_groups_of_same_characters(self):
        # Arrange
        s = "AAABBB"
        expected = 4

        # Act
        result = alternatingCharacters(s)

        # Assert
        self.assertEqual(
            result, expected, f"For string '{s}', should return {expected} deletions"
        )

    def test_empty_string(self):
        # Arrange
        s = ""
        expected = 0

        # Act
        result = alternatingCharacters(s)

        # Assert
        self.assertEqual(
            result, expected, f"For empty string, should return {expected} deletions"
        )

    def test_single_character(self):
        # Arrange
        s = "A"
        expected = 0

        # Act
        result = alternatingCharacters(s)

        # Assert
        self.assertEqual(
            result,
            expected,
            f"For single character string '{s}', should return {expected} deletions",
        )

    def test_mixed_alternating_and_repeating(self):
        # Arrange
        s = "AABAAB"
        expected = 2

        # Act
        result = alternatingCharacters(s)

        # Assert
        self.assertEqual(
            result, expected, f"For string '{s}', should return {expected} deletions"
        )

    def test_long_repeating_sequence(self):
        # Arrange
        s = "AAAABBBBAAABBB"
        expected = 10

        # Act
        result = alternatingCharacters(s)

        # Assert
        self.assertEqual(
            result,
            expected,
            f"For long repeating sequence '{s}', should return {expected} deletions",
        )
