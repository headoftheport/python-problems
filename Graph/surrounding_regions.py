class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            if board[i][0] == "O":
                self.dfs(board, i, 0)
            if board[i][n-1] == "O":
                self.dfs(board, i , n-1)
        
        for i in range(n):
            if board[0][i] == "O":
                self.dfs(board, 0, i)
            if board[m-1][i] == "O":
                self.dfs(board, m-1 , i)
                
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "*":
                    board[i][j] = "O"
                    
                    
                
            
        
        
        
    def dfs(self, board, i, j):
        
        if i < 0 or i > len(board)-1 or j < 0 or j > len(board[0])-1 or board[i][j] != 'O':
            return 
        
        board[i][j] = "*"
        
        self.dfs(board, i+1, j)
        self.dfs(board, i-1, j)
        self.dfs(board, i, j+1)
        self.dfs(board, i, j-1)
        
        
        