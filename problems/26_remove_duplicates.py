'''
# TAG-TWOP
# N.B.  again, we need to read from somewhere and write from somwhere
        initially tried searching from current position, but ran into complexity issues
            - if you search for a unique without updating seen, then you will have to go back and update those ones
        then realised: if it is in-place, then you can just reduce this searching pointer to a naive reading pointer
        and track where you would like to write to

maintain a reading and writing pointer; read in numbers and when you find a unique one, update nums with the writing
pointer and move on
'''

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()

        count = 0
        reading_it = 0
        writing_it = 0
        while reading_it < len(nums):
                        
            n = nums[reading_it]
            if n not in seen:   # if it is unique, then record it, write it and move on
                seen.add(n)
                nums[writing_it] = n

                writing_it += 1
                reading_it += 1

                count += 1
            else:   # if it is not unique, then just continue reading while leaving the writing slot open
                reading_it += 1
        
        return count