"""group anagram"""
import collections

class Solution:
    """solution"""
    def anagrams(self, strs):
        """anagrams"""
        count = collections.Counter([tuple(sorted(s)) for s in strs])
        return filter(lambda x: count[tuple(sorted(x))]>1, strs)


if __name__ == '__main__':
    print(Solution().anagrams(["eat","tea","tan","ate","nat","bat"]))