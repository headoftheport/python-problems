class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        tc: O(m*n*log(D))
        sc: O(1)
        """
        low = matrix[0][0]
        high = matrix[len(matrix)-1][len(matrix[0])-1] + 1;
        
        
        while low < high:
            
            mid = low + (high-low) // 2
            count = 0
            for i in range(len(matrix)):
                j = len(matrix[0]) - 1
                while j >= 0 and matrix[i][j] > mid:
                    j-=1
                    
                count += j + 1
            
            if count < k:
                low = mid + 1
            else:
                high = mid
                
        return low