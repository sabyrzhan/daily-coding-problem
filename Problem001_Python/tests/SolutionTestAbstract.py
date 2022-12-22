class SolutionTestAbstract:
    def testDivision_success(self):
        items = [1, 2, 3, 4, 5]
        expected = [120, 60, 40, 30, 24]
        print(self._getSolution())
        result = self._getSolution().solveProduct(items)
        self.assertEqual(expected, result)

    def testDivision_success2(self):
        items = [3, 2, 1]
        expected = [2, 3, 6]
        result = self._getSolution().solveProduct(items)
        self.assertEqual(expected, result)

    def testDivision_with1element(self):
        items = [0]
        expected = [0]
        result = self._getSolution().solveProduct(items)
        self.assertEqual(expected, result)

    def testDivision_withEmptyArray(self):
        items = []
        expected = []
        result = self._getSolution().solveProduct(items)
        self.assertEqual(expected, result)

    def _getSolution(self):
        raise NotImplementedError("method not implemented")