"""solve polish equation"""
class Solution:
    """solution"""
     def __init__(self):
        self.back = 0
        
    def evalRPN(self, tokens: List[str]) -> int:
        """
        recursion
        O(n)
        O(n)
        """
        self.back = len(tokens)
        return self.helper(tokens)

    
    def helper(self, tokens):
        """helper"""
        self.back = self.back-1
        token = tokens[self.back]
        # print(token)
        if token == "+" or token == "-" or token == "*" or token == "/":
            second = self.helper(tokens)
            first = self.helper(tokens)
            ans = 0
            if token == "+":
                ans = first + second
            elif token == "-":
                ans =  first - second
            elif token == "*":
                ans =  first * second
            elif token == "/":
                ans =  int(first/second) 
            # print(ans)
            return ans

        return int(token)
