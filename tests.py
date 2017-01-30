
import unittest

from bowlingtest import bowling10

SCORE_SET = [  # ([scores], expected)
    ([10, 3, 7, 6, 1, 10, 10, 10, 2, 8, 9, 0, 7, 3, 10, 10, 10], 193),
    ([9, 0, 3, 5, 6, 1, 3, 6, 8, 1, 5, 3, 2, 5, 8, 0, 7, 1, 8, 1], 82),
    ([9, 0, 3, 7, 6, 1, 3, 7, 8, 1, 5, 5, 0, 10, 8, 0, 7, 3, 8, 2, 8], 131),
]


class Bowling10Case(unittest.TestCase):

    def test_01(self):
        """
            Requirement: correct result in case of correct inputs
        """
        for scores, expected in SCORE_SET:
            result = bowling10(scores)
            self.assertEqual(result, expected)


def main():
    unittest.main()

if __name__ == "__main__":
    main()
