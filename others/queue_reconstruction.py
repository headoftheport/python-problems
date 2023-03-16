class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        people.sort(key = lambda p: (p[0], -p[1]))
        ans = [[] for i in range(len(people))]
        for pair in people:
            pos = 0
            j = 0
            while j < len(ans):
                
                if len(ans[j]) == 0:
                    if pos == pair[1]:
                        break
                    pos+= 1
                j+= 1
            # print(j) 
            ans[j] = pair
            # print(ans)
            
        return ans
                
            
            
        
        
        