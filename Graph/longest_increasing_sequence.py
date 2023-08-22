from ast import List
from collections import deque


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        maxLen = 0
        
        store = [[-1 for _ in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                maxLen = max(maxLen, self.iterate(matrix, i, j, -1, store))
                
        return maxLen
                
     
    def iterate(self, matrix, row, col, prevNum, store ):
        
        if row >= len(matrix) or col >= len(matrix[0]):
            return 0
        
        if row < 0 or col < 0:
            return 0
        
        if matrix[row][col] <= prevNum:
            return 0
        
        if store[row][col] != -1:
            return store[row][col]
        
        maxLen = 0
        
        for i, j in [(1,0), (0,1), (-1,0), (0,-1)]:
            
            m = row + i
            n = col + j
            
            nextLen = self.iterate(matrix, m, n, matrix[row][col], store)
            maxLen = max(maxLen, nextLen)
        
        store[row][col] = maxLen + 1  
        return store[row][col]
    
    def longestIncreasingPath2(self, matrix: List[List[int]]) -> int:
        
        
        rows = len(matrix)
        if rows == 0:
            return 0
        
        cols = len(matrix[0])
        directions = [(0,1), (1, 0), (-1,0), (0,-1)]
        indegree = [[0 for i in range(cols)] for j in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                for x, y in directions:
                    nx = i + x
                    ny = j + y
                    if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] < matrix[i][j]:
                        indegree[i][j] += 1
                        
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if indegree[i][j] == 0:
                    queue.append((i,j))
        ans = 0   
        print(indegree)
        while queue:
            sz = len(queue)
            for node in range(sz):
                x, y = queue.popleft()
                for i,j in directions:
                    nx = i + x
                    ny = j + y
                    if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] > matrix[x][y]:
                        indegree[nx][ny] -= 1
                        if indegree[nx][ny] == 0:
                            queue.append((nx, ny))
                            
                            
            ans += 1
            
        return ans