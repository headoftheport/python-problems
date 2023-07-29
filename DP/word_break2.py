class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        ans = []
        curr = []
        self.dfs(s, 0, wordDict, ans, "")
        return ans
    
    
    def dfs(self, s, index, wordDict, ans , string):
        
        if index == len(s):
            ans.append(string)
            return True
        
        for i in range(index, len(s)):
            
            currString = s[index: i+1]
            
            if currString not in wordDict:
                continue
            
            nex = currString if string == "" else string + " " + currString
            self.dfs(s, i+1, wordDict, ans,  nex)
             
        return