import unittest
from src import staircase


class TestStaircase(unittest.TestCase):
    def test_give_2_with_hash_should_be_hh(self):
        # arrange
        n = 2
        pattern = "#"
        expected_output = " #\n" + "##"

        # act
        result = staircase.staircase(n, pattern)

        # assert
        self.assertEqual(result, expected_output, f"Should be {expected_output}")
