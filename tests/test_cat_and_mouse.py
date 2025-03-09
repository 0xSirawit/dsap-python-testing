import unittest
from src.cat_and_mouse import catAndMouse


class TestCatAndMouse(unittest.TestCase):
    def test_cat_a_wins_when_closer(self):
        # Arrange
        cat_a_pos = 2
        cat_b_pos = 8
        mouse_pos = 4
        expected = "Cat A"

        # Act
        result = catAndMouse(cat_a_pos, cat_b_pos, mouse_pos)

        # Assert
        self.assertEqual(
            result, expected, f"When Cat A is closer, should return '{expected}'"
        )

    def test_cat_b_wins_when_closer(self):
        # Arrange
        cat_a_pos = 10
        cat_b_pos = 6
        mouse_pos = 5
        expected = "Cat B"

        # Act
        result = catAndMouse(cat_a_pos, cat_b_pos, mouse_pos)

        # Assert
        self.assertEqual(
            result, expected, f"When Cat B is closer, should return '{expected}'"
        )

    def test_mouse_escapes_when_equidistant(self):
        # Arrange
        cat_a_pos = 3
        cat_b_pos = 7
        mouse_pos = 5
        expected = "Mouse C"

        # Act
        result = catAndMouse(cat_a_pos, cat_b_pos, mouse_pos)

        # Assert
        self.assertEqual(
            result,
            expected,
            f"When both cats are equidistant, should return '{expected}'",
        )

    def test_with_negative_coordinates(self):
        # Arrange
        cat_a_pos = -5
        cat_b_pos = 5
        mouse_pos = -2
        expected = "Cat A"  # Cat A is at distance 3, Cat B is at distance 7

        # Act
        result = catAndMouse(cat_a_pos, cat_b_pos, mouse_pos)

        # Assert
        self.assertEqual(
            result, expected, f"Should handle negative positions correctly"
        )

    def test_with_zero_coordinates(self):
        # Arrange
        cat_a_pos = 0
        cat_b_pos = 6
        mouse_pos = 2
        expected = "Cat A"  # Cat A is at distance 2, Cat B is at distance 4

        # Act
        result = catAndMouse(cat_a_pos, cat_b_pos, mouse_pos)

        # Assert
        self.assertEqual(result, expected, f"Should handle zero positions correctly")
