"""top k elements"""
from heapq import heapify, heappop
from collections import Counter

class Solution:
    """solution"""
    def top_k_elements(self,nums, k):
        """top k elements"""

        store = {}
        for i in nums:
            if i not in store:
                store[i] = Node(i)
            store[i].increase()

        lis = [v for k, v in store.items()]

        heapify(lis)
        ret = []
        for i in range(k):
            ret.append(heappop(lis).data)

        return ret

    def top_k_elements2(self, nums, k):
        """bucket sort"""
        bucket = [[] for _ in range(len(nums) + 1)]
        Count = Counter(nums).items()  
        for num, freq in Count: bucket[freq].append(num) 
        flat_list = [item for sublist in bucket for item in sublist]
        return flat_list[::-1][:k]


class Node:
    """solution"""
    def __init__(self, data) -> None:
        self.data = data
        self.count = 0

    def increase(self):
        """increase"""
        self.count = self.count + 1

    def __lt__(self, nex):
        return self.count > nex.count

