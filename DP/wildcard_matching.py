class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        string = 0
        pattern = 0
        last = -1
        match = 0
        
        
        while string < len(s):
            
            if pattern < len(p) and ( p[pattern] == '?' or p[pattern] == s[string]):
                string += 1
                pattern += 1
            elif pattern < len(p) and p[pattern] == '*':
                last = pattern
                match = string
                pattern += 1
            elif last != -1:
                pattern = last + 1
                match = match + 1
                string = match
            else: 
                return False
        
        
        while pattern < len(p) and p[pattern] == '*':
            pattern  += 1
            
        return pattern == len(p)
            

class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        
        store = [[False for _ in range(len(p)+1)] for j in range(len(s)+1)]
        store[0][0] = True
        
        for i in range(1,len(p)+1):
            if p[i-1] != '*':
                break
            store[0][i] = True
            
            
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                
                if p[j-1] == s[i-1] or p[j-1] == '?':
                    store[i][j] = store[i-1][j-1]
                if p[j-1] == '*':
                    store[i][j] = store[i-1][j] or store[i][j-1]
                    
                
        return store[-1][-1]