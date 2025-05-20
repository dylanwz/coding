'''
# TAG-DIFF
# N.B.:     | i | diff\[i] | prefix sum |
            | - | -------- | ---------- |
            | 0 | 0        | 0          |
            | 1 | +1       | 1          |
            | 2 | 0        | 1          |
            | 3 | 0        | 1          |
            | 4 | -1       | 0          |
            | 5 | 0        | 0          |
'''
from typing import List
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n+1)

        for q in queries:
            ql = q[0]
            qr = q[1]
            diff[ql] += 1
            diff[qr + 1] -= 1
        
        # turn it into a prefix-sum
        for idx in range(1, n+1):
            diff[idx] = diff[idx - 1] + diff[idx]

        for idx in range(n):
            if (nums[idx] - diff[idx]) > 0:
                return False
        
        return True