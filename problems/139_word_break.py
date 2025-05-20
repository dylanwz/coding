'''
# TAG-DP
# N.B.: you have
- subproblem: can i solve a smaller version of this problem (like a trivial one)? is it any easier?
- recurrence: how can i solve a larger version using only what i know about the smaller version?
- base case: until i cannot use any smaller version
'''

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for it1 in range(1, len(s) + 1):
            for it2 in range(it1):
                if (dp[it2] is True) and (s[it2:it1] in words):
                    dp[it1] = True
                    break

        return dp[len(s)]