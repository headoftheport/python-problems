"""pascal triangle 2"""
class Solution:
    """solution"""
    def get_row(self, row_index):
        """recursive solution""" 
        if row_index == 0:
            return [1]
        
        array = self.get_row(row_index-1)
        return_array = []
        for i in range(row_index+1):
            if i == 0 or i == row_index:
                return_array.append(1)
            else:
                return_array.append(array[i-1] + array[i])
        return return_array


    def get_row2(self, row_index):
        """iterative solution"""
        #space complexity is 0(n)
        #time complexity is 
        array = [1]
        for i in range(row_index+1):
            temp = list()
            for j in range(i+1):
                if j == 0 or j == i+1:
                    temp.append(1)
                else:
                    temp.append(array[i-1] + array[i])
            array = temp
        return array


    def get_row3(self, row_index):
        """linear solution"""
        nCk = 1
        array = list()
        for i in range(row_index+1):
            array.append((int(nCk)))
            nCk = nCk * (row_index - i) / (i+1)

        return array


print(Solution().get_row3(4))