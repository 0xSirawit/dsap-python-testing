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

    def test_give_1_with_hash(self):
        # arrange
        n = 1
        pattern = "#"
        expected_output = """#"""

        # act
        result = staircase.staircase(n, pattern)

        # assert
        self.assertEqual(result, expected_output, f"Should be {expected_output}")

    def test_give_3_with_hash(self):
        # arrange
        n = 3
        pattern = "#"
        expected_output = """  #
 ##
###"""

        # act
        result = staircase.staircase(n, pattern)

        # assert
        self.assertEqual(result, expected_output, f"Should be {expected_output}")

    def test_give_10_with_star(self):
        # arrange
        n = 10
        pattern = "*"
        expected_output = """         *
        **
       ***
      ****
     *****
    ******
   *******
  ********
 *********
**********"""

        # act
        result = staircase.staircase(n, pattern)

        # assert
        self.assertEqual(result, expected_output, f"Should be {expected_output}")

    def test_give_30_with_dollar(self):
        # arrange
        n = 30
        pattern = "$"
        # Hardcoded expected output for n=30
        expected_output = """                             $
                            $$
                           $$$
                          $$$$
                         $$$$$
                        $$$$$$
                       $$$$$$$
                      $$$$$$$$
                     $$$$$$$$$
                    $$$$$$$$$$
                   $$$$$$$$$$$
                  $$$$$$$$$$$$
                 $$$$$$$$$$$$$
                $$$$$$$$$$$$$$
               $$$$$$$$$$$$$$$
              $$$$$$$$$$$$$$$$
             $$$$$$$$$$$$$$$$$
            $$$$$$$$$$$$$$$$$$
           $$$$$$$$$$$$$$$$$$$
          $$$$$$$$$$$$$$$$$$$$
         $$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$
       $$$$$$$$$$$$$$$$$$$$$$$
      $$$$$$$$$$$$$$$$$$$$$$$$
     $$$$$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$$
   $$$$$$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$$$$$$
 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"""

        # act
        result = staircase.staircase(n, pattern)

        # assert
        self.assertEqual(
            result, expected_output, f"Should produce correct staircase for n=30"
        )

    def test_give_5_with_at(self):
        # arrange
        n = 5
        pattern = "@"
        expected_output = """    @
   @@
  @@@
 @@@@
@@@@@"""

        # act
        result = staircase.staircase(n, pattern)

        # assert
        self.assertEqual(result, expected_output, f"Should be {expected_output}")

    def test_give_4_with_caret(self):
        # arrange
        n = 4
        pattern = "^"
        expected_output = """   ^
  ^^
 ^^^
^^^^"""

        # act
        result = staircase.staircase(n, pattern)

        # assert
        self.assertEqual(result, expected_output, f"Should be {expected_output}")

    def test_give_15_with_plus(self):
        # arrange
        n = 15
        pattern = "+"
        expected_output = """              +
             ++
            +++
           ++++
          +++++
         ++++++
        +++++++
       ++++++++
      +++++++++
     ++++++++++
    +++++++++++
   ++++++++++++
  +++++++++++++
 ++++++++++++++
+++++++++++++++"""

        # act
        result = staircase.staircase(n, pattern)

        # assert
        self.assertEqual(result, expected_output, f"Should be {expected_output}")
