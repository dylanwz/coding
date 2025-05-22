'''
# TAG-DP
# N.B.

"at each index I can either take it or leave it"
subproblem: best value up to house i
recurrence: if i take it, then i have dp[i-2] + current; otherwise, it's dp[i-1]
'''

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range (2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        return dp[-1] 