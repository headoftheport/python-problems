"""Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses."""
class Solution:
    """solution"""
    def __init__(self):
        """init"""
        self.memo = [[] for i in range(9)]
        
    def generate_parentheses3(self, n: int):
        """DP solution"""
        store = []

        if n == 0:
            store.append("")
        elif len(self.memo[n]) > 0:
            return self.memo[n]
        else:
            for c in range(n):
                for left in self.generate_parentheses3(c): 
                    for right in self.generate_parentheses3(n-c-1):
                        store.append( '(' + left + ')' + right)
        self.memo[n] = store           
        return store
    
    def generate_parentheses(self, n: int):
        """recursive """
        store = []
        stack = []
        def backtrack(openCount, closedCount):
            
            if openCount == n and closedCount == n:
                store.append(''.join(stack))
                return
            
            if openCount < n:
                stack.append('(')
                backtrack(openCount+1, closedCount)
                stack.pop()
                
            if closedCount < openCount:
                stack.append(')')
                backtrack(openCount, closedCount+1)
                stack.pop()
                
            return
        
        backtrack(0,0)
        return store

    def generate_parentheses2(self, n: int) -> List[str]:
        """Brute Force"""
        store = []
        self.recur(store, '(', n)
        return store
           
    def recur(self, store, string, n):
        """recursion"""
        if len(string) == 2*n - 1:
            
            if self.valid(string + ")"):
                store.append(string + ')')
                return
            else:
                return
       
        
        self.recur(store, string + '(', n)
        self.recur(store, string + ')', n)
        
        return
           
    def valid(self, string):
        """validity"""
        stack = []
        for i in string:
            if i == "(":
                stack.append(")")
                continue
            if len(stack) == 0:
                return False
            stack.pop()
            
        return len(stack) == 0