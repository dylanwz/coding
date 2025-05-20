'''
# TAG-BACKTRACKING
# N.B.: pop, base case, explore valid options (natural abandonment if no remaining valid)
'''

from typing import List

class Solution:
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)

        res = []
        for idx in range(0, len(candidates)):
            
            # organise paths by the index they start on; skip starting on duplicates
            if idx == 0 or candidates[idx] != candidates[idx-1]:
                stack = [(idx, [candidates[idx]], candidates[idx])]
            else:
                continue

            while stack:
                i, path, total = stack.pop() # get most recent state to explore

                # base case (solution)
                if total == target:
                    if path not in res:
                        res.append(path)
                    continue


                # explore valid options... everything from the index that the current path has explored is valid
                # as long as it doesn't surpass the target (since sorted)
                # e.g. for [1,1,2,5,6] and t=8:     we will have at some point 1 1 2, 1 1 5, 1 1 6
                for j in range(i+1, len(candidates)):

                    # adding duplicate numbers to the current path is pointless
                    if j > i+1 and candidates[j] == candidates[j-1]:
                        continue
                    if total + candidates[j] > target:
                        break
                    stack.append((j, path + [candidates[j]], total + candidates[j]))
        
                # if no remaining options, nothing will be added and something will popped
                # i.e. natural abandonment
        return res

                
                
                
