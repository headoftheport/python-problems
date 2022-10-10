"""find path"""
class Solution:
    """solution"""
    def find_path(self,  m,  n):
        """
        tabulation
        time:0(m*n)
        space: O(m*n)
        """
        grid = [[0 for i in range(n)] for j in range (m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    grid[i][j] = 1
                else:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]

        return grid[m-1][n-1]
