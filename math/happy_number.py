"""happy number"""
class Solution:
    """solution"""
    def is_happy(self, num):
        """solve it by checking the cycle"""
        path = {}
        sumValue = num
        while sumValue != 1:
            temp = 0
            while sumValue > 0:
                temp += pow(sumValue%10,2)
                sumValue = sumValue // 10
                
            if temp in path:
                return False
            path[temp] = 1
            sumValue = temp
            
        return True