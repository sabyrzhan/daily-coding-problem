from unittest import TestCase

from Solution import SolutionWithDivision
from tests.SolutionTestAbstract import SolutionTestAbstract


class SolutionTestWithoutDivision(SolutionTestAbstract, TestCase):
    def _getSolution(self):
        return SolutionWithDivision()
