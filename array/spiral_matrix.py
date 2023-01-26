class Solution:
    def spiralOrder(self, matrix):
        """
            tc : m*n
            sc : m*n 
        """
        res = []
        row = len(matrix)
        col = len(matrix[0])
        
        if row == 0:
            return res
        
        if col == 0:
            return  res
        
        
        vector = [[0,1], [1, 0], [0, -1], [-1, 0]]
        curr = 0
        pos = [col, row-1]
        rowCurr = 0
        colCurr = -1
        
        while pos[curr%2]:
            
            for i in range(pos[curr%2]):
                rowCurr += vector[curr][0]
                colCurr += vector[curr][1]
                res.append(matrix[rowCurr][colCurr])
                
            pos[curr%2] = pos[curr%2]-1
            curr = (curr + 1) % 4
            
        return res
        
        