'''
# TAG-DP
# N.B.

subproblem: longest subsequence ending at index i
recurrence: for some j < i, if current arr[i] is less than any arr[j] then longest is dp[j] + 1 
'''

from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # subproblem: longest increasing subsequence ending at index i
        
        n = len(nums)
        if n == 1:
            return 1

        dp = [1] * n

        res = float('-inf')
        for i in range(n):
            if i == 0:
                continue
            mx = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] >= mx:
                        mx = dp[j] + 1
            dp[i] = mx
            if dp[i] > res:
                res = dp[i]
        return res