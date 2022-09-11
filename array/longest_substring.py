"""longest substring without repeating characters"""
class Solution:
    """solution"""
    def longest_substring(self, string):
        """
        iterative solution
        time complexity: O(n)
        space complexity: O(n)
        """
        store = dict()
        count = 0
        last_duplicate = -1
        for index in enumerate(len(string)):
            if string[index] not in store:
                store[string[index]] = index
            else:
                last_duplicate = max(last_duplicate, store[string[index]])
                store[string[index]] = index
            count = max(count, index - last_duplicate)

        return count

