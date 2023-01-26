class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        temp = []
        total = 0
        for num in nums:
            total += num
            temp.append(total)


        ans = []
        for num in queries:
            ans.append(self.binary_search(temp,num))

        return ans

    def binary_search(self, arr, val):

        start = 0
        end = len(arr)-1
        pos = 0
        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] == val:
                pos = mid + 1
                break
            if arr[mid] < val:
                pos = mid+1
                start = mid + 1
            else:
                end = mid - 1

        return pos