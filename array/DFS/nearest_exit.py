""""neartest exit in the maze"""
from collections import deque 
class Solution:
    """solution"""
    def nearest_exit(self, maze, entrance):
        """
            DFS 
            tc: O(m*n)
            sc: O(max(m,n)
        """
        queue = deque()
        row = len(maze)
        col = len(maze[0])
        queue.append((entrance[0], entrance[1]))
        maze[entrance[0]][entrance[1]] = '+'
        direction = [1, 0, -1, 0, 1]
        step = 0
        while queue:
            step = step + 1
            n = len(queue)
            for i in range(n):
                curr = queue.popleft()
                
                for i in range(4):

                    x = curr[0]+direction[i]
                    y = curr[1]+direction[i+1]

                    if x < 0 or y < 0 or x >= row or y >= col:
                        continue

                    if maze[x][y] == "+":
                        continue

                    if maze[x][y] == "." and ( x == 0 or y == 0 or x == row-1 or y == col-1):
                        return step

                    
                    maze[x][y] = '+'
                    queue.append((x, y))


        return -1
    

                
