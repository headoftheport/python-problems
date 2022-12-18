class Solution:
    def partition(self, s: str):

        return self.partition_string(s, 0)


    def partition_string(self, s, pos):

        if pos >= len(s):
            return [[]]

        curr = pos
        return_list = []
        string = ""
        while curr < len(s):
            string += s[curr]
            if self.is_palindrome(s, pos, curr):
                temp = self.partition_string(s, curr+1)
                for i in temp:
                    i.insert(0, string)
                    return_list.append(i)

            curr += 1

        return return_list
                


    def is_palindrome(self, s, start, end):

        for i in range(0, (end-start) // 2 +1):
            if s[start+i] != s[end-i]:
                return False
        return True

