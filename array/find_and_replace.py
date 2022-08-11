class Solution:
    def findAndReplacePattern(self, words, pattern: str):
        
        
        ret = list()
        for word in words:
            store = dict()
            store2 = dict()
            found = True
            for i,j in zip(pattern,word):
                
                if i in store and store[i] != j:
                    found = False
                    break
                if j in store2 and store2[j] != i:
                    found = False
                    
                store[i] = j
                store2[j] = i
                
                
            if found:
                ret.append(word)
                
        return ret


    def findAndReplacePattern2(self, words: List[str], pattern: str) -> List[str]:
        
            def encode(string):
                val = 0
                store = {}
                ans = ''
                
                for i in string:
                    if i not in store:
                        store[i] = val
                        val = val + 1
                        
                    ans += str(store[i])
                    
                return ans
            
            ans = encode(pattern)
            ret = list()
            for word in words:
                if encode(word) == ans:
                    ret.append(word)
                    
            return ret
                
                
                
                
        