class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        """
        dfs
        tc: n^3
        sc: len(word)
        """
        dp = [-1 for _ in range(len(s))]
        return self.dfs(s, 0, wordDict, dp)
    
    
    def dfs(self, s, index, wordDict, dp):
        
        if index == len(s):
            return True
        
        if dp[index] != -1:
            return True if dp[index] == 1 else False
        
        result = False
        for i in range(index, len(s)):
            
            currString = s[index: i+1]
            # print(currString)
            if currString not in wordDict:
                continue
                
            if self.dfs(s, i+1, wordDict, dp):
                result = True
                break
        
        if result:
            dp[index] = 1
        else:
            dp[index] = 0
            
        return result
    
class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        """
        dfs
        tc: n + m * k
        sc: len(word)
        """
        dp = [0 for _ in range(len(s))]

        for i in range(len(s)):

            for word in wordDict:

                if i < (len(word)-1):
                    continue

                if i == len(word) - 1 or dp[i-len(word)]:
                   
                    if s[i-len(word)+1: i+1] == word:
                        dp[i] = 1
                        break

        return dp[len(s)-1]
                
        
                
        