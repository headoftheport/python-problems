"""search 2d matrix"""
class Solution:
    """solution"""
    def search(self, matrix, target):
        """
        time: O(n)
        """

        col = len(matrix[0]) - 1
        row = 0

        while row < len(matrix) and col >=0:

            if matrix[row][col] == target:
                return True

            if target < matrix[row][col]:
                col -= 1
            else:
                row += 1