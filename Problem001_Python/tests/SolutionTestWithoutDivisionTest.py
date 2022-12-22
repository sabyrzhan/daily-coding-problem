from unittest import TestCase

from Solution import SolutionWithoutDivision
from tests.SolutionTestAbstract import SolutionTestAbstract


class SolutionTestWithoutDivision(SolutionTestAbstract, TestCase):
    def _getSolution(self):
        return SolutionWithoutDivision()
