'''
# TAG-TWOP
# N.B.  we can see it's two pointer because we need to perform two, separate walks (of one or more arrays)
#       moreover, we want to traverse backwards because if we traverse forwards, then we wil mutate the things we want
#       to traverse to
'''


from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        it1 = m - 1
        it2 = n - 1
        it_res = m + n - 1

        while it1 >= 0:
            if it2 < 0: # then first elt of nums2 is bigger than last elt of nums1
                break
            if nums1[it1] >= nums2[it2]:
                nums1[it_res] = nums1[it1]
                it1 -= 1
            else:
                nums1[it_res] = nums2[it2]
                it2 -= 1
            it_res -= 1

        while it2 >= 0:
            nums1[it_res] = nums2[it2]
            it_res -= 1
            it2 -= 1