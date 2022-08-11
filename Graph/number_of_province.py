class Solution:
    def findCircleNum(self, isConnected) -> int:
        
        seen = [False for i in range(len(isConnected))]
        province = 0
        stack = []
        for i in range(len(isConnected)):
            if seen[i]:
                continue
            province = province + 1
            stack.append(i)
            while len(stack) > 0:
                num = stack.pop()
                seen[num] = True
                for j in range(len(isConnected)):
                    if seen[j] == False and isConnected[num][j]:
                        stack.append(j)
                    
        return province