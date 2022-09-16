"""total fruit in the basket"""
class Solution:
    """solution"""
    def total_fruit(self, fruits) -> int:
        """
        sliding window problem
        best time complexity: O(len(fruits))
        average/worst time complexity: O(len(fruits) + len(not making to basket))
        space complexity: 0(len(unique fruit trees))
        """
        store = {}
        start = 0
        res = 0
        for index,val in enumerate(fruits):
            store[val] = store.get(val, 0) + 1
            while len(store) > 2:
                store[fruits[start]] = store[fruits[start]]-1
                if store[fruits[start]] == 0:
                    del store[fruits[start]]
                start = start + 1
                
            res = max(res, index - start + 1)
            
        return res
                    