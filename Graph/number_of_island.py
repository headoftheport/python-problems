"""total number of island using union find"""
class UnionFind:
    """uninon find"""
    def __init__(self, size) -> None:
        self.root = [-1 for _ in range(size)]

    def find(self,node):
        """find"""
        if node == self.root[node]:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, x,  y):
        """union"""
        findX = self.find(x)
        findY = self.find(y)
        #if both have the same parent they are already linked
        #this also indicates the presence of a loop in the undirected graph
        if findX == findY:
            return False

        self.root[findY] = findX
        return True


class Solution:
    """solution"""
    def number_of_island(self, nums):
        """union find"""
        row = len(nums)
        column = len(nums[0])
        uf = UnionFind(row*column)
        count = 0
        for i in range(row):
            for j in range(column):
                if nums[i][j] == '1':
                    #counts the individual island
                    count += 1

                    if i+1 < row and nums[i+1][j] == '1':
                        #if the value below to current value is also an island which is not linked with current node
                        uf.union(i*column+j, (i+1)*column+j)
                        count -= 1
                    
                    if j+1 < column and nums[i][j+1] == '1':
                        #if the value next to current value is also an island which is not linked with current node
                        uf.union(i*column+j, i*column+j+1)
                        count -= 1
                    
                    #count would go the negative at times but eventually the remaining are the total number of disjoin sets which do not get linked
        return count

