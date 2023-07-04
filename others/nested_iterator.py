# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [[nestedList, 0]]
    
    def next(self) -> int:
        print(len(self.stack))
        self.hasNext()
        node, i = self.stack[-1]
        self.stack[-1][1] = i+1
        return node[i].getInteger()
    
    def hasNext(self) -> bool:
        # s = self.stack 
        while self.stack:
            nestedList, i = self.stack[-1]
            if i == len(nestedList):
                self.stack.pop()
                continue
            
            if nestedList[i].isInteger():
                return True
            
            self.stack[-1][1] = i + 1
            self.stack.append([nestedList[i].getList(),0])
            
        return False
            
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())