'''
# TAG-HEAP
# N.B. a min-heap of size k always contains the k smallest elements (even after O(log n) insertions),
# so ensuring the top of the heap is the, otherwise, largest element means it is the kth largest
# (so reduces problem to only finding the largest)
'''

import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)

        return min_heap[0]
