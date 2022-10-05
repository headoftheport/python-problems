"""solution"""
class Solution:
    """solution"""
    def longest_pal_substring(self, s):
        """expand around centre
        time: O(n2)
        space: O(n2)
        """
        dp = [ [ False for j in range(len(s)) ] for i in range(len(s)) ]
        for i in range(len(s)):
            dp[i][i] = True
        start, end = 0, 0
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                # print(i, j)
                dp[i][j] = (s[i] == s[j]) and ( j - i < 3 or dp[i+1][j-1])
                # print(i, j, dp[i][j])
                if dp[i][j] and j - i > end - start:
                    # print("ans" , i, j)
                    start = i
                    end = j

        return s[start:end+1]


    def longest_pal_substring2(self, s):
        """
        expand around centre
        o(n2)
        o(1)
        """
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expand_around_centre(s, i, i)
            len2 = self.expand_around_centre(s, i, i+1)
            maxim = max(len1, len2)
            if end - start < maxim:
                start = i - (maxim-1) // 2
                end = i + (maxim) // 2

        return s[start:end+1]



    def expand_around_centre(self, s, i, j):
        """
        find palindrome
        """
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1

        return j - i - 1
