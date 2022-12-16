"""valid sudoku"""
class Solution:
    """solution"""
    def isValidSudoku(self, board):


        for i in range(9):
            for j in range(9):
                if board[i][j] != '.' and not self.valid(board, i, j):
                    return False

        return True

    def valid(self, board, row, col):

        for i in range(9):
            if i != row and board[i][col] == board[row][col]:
                return False

            if i != col and board[row][i] == board[row][col]:
                return False


        row_start = row // 3 * 3
        col_start = col // 3 * 3

        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if i != row and col != j and board[row][col] == board[i][j]:
                    return False

        return True


    def isValidSudoku2(self, board) -> bool:
        
        store = set()

        for i in range(0,9):
            for j in range(0,9):
                
                curr = board[i][j]
                
                if curr == '.':
                    continue
                
                if (i,curr) in store or (curr,j) in store or (i//3, j//3 ,curr) in store:
                    return False
                
                store.add((i,curr))
                store.add((curr, j))
                store.add((i//3, j//3 , curr))
                
                
        return True

