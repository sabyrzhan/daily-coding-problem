import unittest

from Solution import Solution


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def testDivision_success(self):
        items = [1, 2, 3, 4, 5]
        expected = [120, 60, 40, 30, 24]
        result = self.solution.solveProductWithDivision(items)
        self.assertEqual(expected, result)

    def testDivision_success2(self):
        items = [3, 2, 1]
        expected = [2, 3, 6]
        result = self.solution.solveProductWithDivision(items)
        self.assertEqual(expected, result)

    def testDivision_with1element(self):
        items = [0]
        expected = [0]
        result = self.solution.solveProductWithDivision(items)
        self.assertEqual(expected, result)

    def testDivision_withEmptyArray(self):
        items = []
        expected = []
        result = self.solution.solveProductWithDivision(items)
        self.assertEqual(expected, result)
