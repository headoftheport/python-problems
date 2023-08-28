from math import ceil, floor

class Solution:
    def calculate(self, s: str) -> int:
        """
        tc: n
        sc: n
        """
        num = 0
        stack = []
        operation = "+"
        for index, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            
            if not char.isdigit() and  char != " " or index == len(s) - 1 :

                if operation == "+":
                    stack.append(num)
                elif operation == "-":
                    stack.append(-num)
                elif operation == "*":
                    stack.append(stack.pop() * num)
                elif operation == "/":
                    div = stack.pop() / num
                    ans = ceil( div ) if div < 0 else floor(div)
                    stack.append(ans)

                operation = char
                num = 0
       
        result = 0

        while stack:
            result += stack.pop()

        return result
    