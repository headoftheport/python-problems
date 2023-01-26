class Solution:
    def maxPoints(self, points) -> int:
        
        if len(points)==1:
            return 1
        
        maxLen = 0
        for i in range(len(points)):
            store = {}
            for j in range(i+1, len(points)):
                slope  = self.findSlope(points[i], points[j])
                if slope not in store:
                    store[slope] =  0   
                store[slope] += 1
                maxLen = max(store[slope], maxLen)
                      
        return maxLen + 1
    
    
    def findSlope(self, point1, point2):
        x, y = point1[0], point1[1]
        x1, y1 = point2[0], point2[1]
        
        if x == x1: return 0
        if y == y1: return float("inf")
        
        return (x - x1) / (y - y1)
        