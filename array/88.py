from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m==0:
            for idx, elem in enumerate(nums1):
                nums1[idx] = nums2[idx]
            return
        elif n==0:
            return
        #Set Indices
        i = m-1
        j = n-1
        #Traverse in reverse
        for x in range(n+m-1, -1, -1):
            if i < 0:
                nums1[x] = nums2[j]
                j = j -1
            elif j < 0:
                nums1[x] = nums1[i]
                i = i -1
            elif nums1[i] < nums2[j]:
                nums1[x] = nums2[j]
                j = j-1
            else:
                nums1[x] = nums1[i]
                i = i-1