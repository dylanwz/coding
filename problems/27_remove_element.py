'''
# TAG-TWOP
# N.B.: we can guess it's two-pointers because we need to do in-place modifications, so we need to read in one or more
#       places (i.e. two, one for reading, and one for checking), and we need to insert in another place
        in this case, we happen to be able to insert where we read... for 88, we need another pointer to do so

have two pointers, one to traverse and another that records the last valid index
- (everything past this index is invalid, but there may still be invalid ones before this index)
while the traversing pointer has not reached the last valid index, we check if the next index is valid
- if it isn't, then swap it with the last valid index
- otherwise, keep going
'''

from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return

        running_it = 0
        end_it = len(nums) - 1
        while (end_it >= 0 and nums[end_it] == val):
            end_it -= 1
        # end_it set to the last valid index
        
        if end_it < 0: # if it is less than 0, then there are no valid indexes
            return 0

        count = 0
        while running_it <= end_it:  # while we are still before the last valid index 
            print(f"{running_it}, {end_it}")
            if nums[running_it] != val:    # if elt is OK, nothing needs to be done
                running_it += 1
            else:   # otherwise, swap it with the last valid index
                tmp = nums[running_it]
                nums[running_it] = nums[end_it]

                # update last valid index
                end_it -= 1
                while (end_it >= 0 and nums[end_it] == val):
                    end_it -= 1
                running_it += 1
            count += 1
        print(f"{running_it}, {end_it}")
        return count
