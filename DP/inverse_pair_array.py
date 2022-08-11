class Solution:
        
    def kInversePairs(self, n: int, k: int) -> int:
        
        memo = [[0 for i in range(10)] for j in range(10)]
        
        for i in range(1,n+1):
            for j in range(0,k+1):
                if j == 0:
                    memo[i][j] = 1
                else:
                    val = min(j, i-1)
                    for p in range(val+1):
                        memo[i][j] = ( memo[i][j] + memo[i-1][j-p] ) % 1000000007
                        
    
        return memo[n][k]
                   

print(Solution().kInversePairs(5,4))



#shallow array concept
#https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/