"""backtrack word search"""
class Solution:
    """solution"""

    def word_search(self, board, word):
        """
        backtrack
        time: (m*n)^3
        space: m*n
        """
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.search(board, i, j, visited, word, 0):
                    return True

        return False


    def search(self,board, i, j, visited, word, index):
        if index == len(word):
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or word[index] != board[i][j]:
            return False

        visited[i][j] = True
        if self.search(board, i+1, j, visited, word, index+1):
            return True
        if self.search(board, i-1, j, visited, word, index+1):
            return True
        if self.search(board, i, j+1, visited, word, index+1):
            return True
        if self.search(board, i, j-1, visited, word, index+1):
            return True
        visited[i][j] = False
        return False

        