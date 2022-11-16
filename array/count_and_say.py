"""count and say"""
class Solution:
    """solution"""
    def count_and_say(self, n):
        val = "1"
        for _ in range(1, n):
            val = self.helper(val)

        return val

    def helper(self, val):
        string = ""
        count = 0
        char = val[0]
        for i in val:
            if char == i:
                count = count + 1
            else:
                string += str(count)
                string += char
                char = i
                count = 1

        string += str(count)
        string += char
        return val

        