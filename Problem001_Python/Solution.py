"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


class SolutionWithDivision:
    def solveProduct(self, items = []):
        total = 1
        containsZero = False
        for v in items:
            total *= v
            if v == 0:
                containsZero = True

        for i in range(len(items)):
            if containsZero:
                items[i] = 0
            else:
                items[i] = total / items[i]

        return items


class SolutionWithoutDivision:
    def solveProduct(self, items = []):
        total = 1
        containsZero = False
        for v in items:
            total *= v
            if v == 0:
                containsZero = True

        for i in range(len(items)):
            if containsZero:
                items[i] = 0
            else:
                items[i] = self.__divideNumber(total, items[i])

        return items

    def __divideNumber(self, divident, divisor):
        quotient = 0
        while(divident >= divisor):
            divident = divident - divisor
            quotient += 1

        return quotient
