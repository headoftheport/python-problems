"""Letter Combinations of a Phone Number"""
class Solution:
    """solution"""

    def __init__(self):
        self.store = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz"   
        }


    def letter_combinations(self, digits):
        """fist answer"""
        
        return self.helper(digits)
        
       
    def helper(self, string):
        """helper method"""
        if len(string) == 0:
            return []
        if len(string) == 1:
            return [*self.store[string[0]]]
        
        values = self.helper(string[1:])
        return_values = list()
        for char in self.store[string[0]]:
            for item in values:
                temp = char + item
                return_values.append(temp)
            
        return return_values


    
    def letter_combinations2(self, digits):
        """backtrack solution"""
        combinations = []

        if len(digits) == 0:
            return combinations

        def backtrack(index, string):

            if len(string) == len(digits):
                combinations.append(string)
                return

            
            for char in self.store[digits[index]]:
                backtrack( index + 1, string + char)

            return

        backtrack(0, "")
        return combinations



        


