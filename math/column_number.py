"""solution"""

from functools import reduce

class Solution:
    """solution"""
    def title_to_number(self, column_title: str) -> int:
        """iterative solution"""
        func = lambda x, y: x * 26 + y
        nums = [ord(c)-64 for c in list(column_title)]
        return reduce(func,nums)

    def title_to_number2(self, column_title: str) -> int:
        """iterative solution"""
        col_number = 0
        for c in list(column_title):
            col_number *= 26
            col_number += ord(c) - 64
        return col_number