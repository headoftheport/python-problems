"""task scheduler"""
from heapq import heappop, heappush, heappushpop, heapify
from collections import Counter
class Solution:
    """solution"""
    def task_scheduler(self,tasks, n):
        """using pq"""

        curr_time = 0
        heap = []
        store = Counter(tasks)

        for k, v in store.items():
            heappush(heap, (-1*v, k))

        while heap:

            interval = n + 1
            task_count = []

            while interval > 0 and heap:
                curr_time += 1
                count, task = heappop(heap)
                if count != -1:
                    task_count.append((count+1, task))
                interval -= 1

            for item in task_count:
                heappush(heap, item)

            if len(heap) == 0:
                break
                
            curr_time += interval

        return curr_time


    def task_scheduler2(self, tasks, n):
        """using math"""
        store = Counter(tasks)
        max_count = max(store.values())
        max_task = sum([1 for x in store.values() if x == max_count])

        return max(len(tasks), (max_count - 1) * (n + 1) + max_task)


                
        
            