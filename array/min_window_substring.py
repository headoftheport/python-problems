class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        two pointer 
        tc: t^2
        sc: 1 
        """
        store = [0 for _ in range(128)]
        
        for char in t:
            store[ord(char)] += 1
            
        
        start = 0
        end = 0
        counter = len(t)
        ans = ""
        
        for end in range(len(s)):
            
            if store[ord(s[end])] > 0:
                counter -= 1
                
            store[ord(s[end])] -= 1
            
            while counter == 0:
                window_size = end - start + 1
                if ans == "" or len(ans) > window_size:
                    ans = s[start:end+1]
                    
                store[ord(s[start])] += 1
                if store[ord(s[start])] > 0:
                    counter += 1
                    
                start += 1
                    
        return ans
                
        