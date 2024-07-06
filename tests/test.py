import unittest
from my_sum import sum
from fractions import Fraction


class TestMySum(unittest.TestCase):
    def test_my_sum(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(1, 2)]
        result = sum(data)
        self.assertEqual(result, 1)

    def test_bad_type(self):
        """
        test will pass if sum(data) raises TypeError
        can replace typeerror with any other exception you choose
        """
        data = "banana"
        with self.assertRaises(TypeError):
            sum(data)


if __name__ == "__main__":  # command line entry point
    unittest.main()
