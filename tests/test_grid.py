import unittest
from src.grid import gridChallenge


class TestGridChallenge(unittest.TestCase):
    def test_example_case(self):
        # Arrange
        grid = ["a b c", "a d e", "e f g"]
        expected = "YES"

        # Act
        result = gridChallenge(grid)

        # Assert
        self.assertEqual(result, expected, f"Should return '{expected}'")

    def test_sample_input(self):
        # Arrange
        grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]
        expected = "YES"

        # Act
        result = gridChallenge(grid)

        # Assert
        self.assertEqual(result, expected, f"Should return '{expected}'")

    def test_already_sorted_grid(self):
        # Arrange
        grid = ["abc", "def", "ghi"]
        expected = "YES"

        # Act
        result = gridChallenge(grid)

        # Assert
        self.assertEqual(
            result, expected, f"Already sorted grid should return '{expected}'"
        )

    def test_unsorted_columns(self):
        # Arrange
        grid = ["cba", "def", "ghi"]
        expected = "YES"

        # Act
        result = gridChallenge(grid)

        # Assert
        self.assertEqual(
            result, expected, f"Unsorted columns should return '{expected}'"
        )

    def test_single_row_grid(self):
        # Arrange
        grid = ["zyxwvutsrqponmlkjihgfedcba"]
        expected = "YES"

        # Act
        result = gridChallenge(grid)

        # Assert
        self.assertEqual(result, expected, f"Single row should return '{expected}'")

    def test_single_column_grid(self):
        # Arrange
        grid = ["z", "y", "x", "w", "v"]
        expected = "NO"

        # Act
        result = gridChallenge(grid)

        # Assert
        self.assertEqual(
            result,
            expected,
            f"Single column descending should return '{expected}'",
        )

    def test_with_repeated_characters(self):
        # Arrange
        grid = ["aaa", "bbb", "ccc"]
        expected = "YES"

        # Act
        result = gridChallenge(grid)

        # Assert
        self.assertEqual(
            result,
            expected,
            f"Grid with repeated chars should return '{expected}'",
        )
