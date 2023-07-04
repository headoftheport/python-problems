class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        """
        union find
        tc: n * n 
        sc: n
        """
        uf = UnionFind(len(isConnected))
        count = len(isConnected)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if(isConnected[i][j] and (not uf.isLinked(i, j))):
                    count -= 1
                    uf.union(i,j)
                
        return count
    

    def findCircleNum2(self, isConnected: List[List[int]]) -> int:
        
        """
        dfs
        tc: n*n
        sc: n
        """
        visited = [False for i in range(len(isConnected))]
        count = 0
        for i in range(len(isConnected)):
            
            if( not visited[i]):
                count += 1
                self.dfs(visited, i, isConnected)
                
        return count
    
    
    def dfs(self, visited, curr, isConnected):
        
        visited[curr] = True
        
        for i in range(len(isConnected)):
            if(not visited[i] and isConnected[curr][i] == 1):
                self.dfs(visited, i, isConnected)
    
    
class UnionFind:


    def __init__(self, n):
        self.store = [i for i in range(n)]


    def union(self, x, y):
        
        parentX = self.find(x)
        parentY = self.find(y)

        if parentX == parentY:
            return;

        self.store[parentY] = parentX    

    def find(self, x):

        if self.store[x] == x:
            return x
        temp = self.store[x]
        self.store[x] = self.find(temp)
        return self.store[x]
    
    def isLinked(self, x, y):
        return self.find(x) == self.find(y)


    def getStore(self):
        return self.store
        