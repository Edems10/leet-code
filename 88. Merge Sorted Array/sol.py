from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        elif n == 0:
            return
        second_iter = 0
        for i in range(m+n):
            if i >= m:
                nums1[i] = nums2[second_iter]
                second_iter = second_iter +1
            elif nums1[i]>nums2[second_iter]:
                temp = nums1[i]
                nums1[i]=nums2[second_iter]
                nums2[second_iter] = temp
                if second_iter<n-1:
                    temp_iter = second_iter+1
                    while(temp>nums2[temp_iter]):
                        nums2[temp_iter-1] = nums2[temp_iter]
                        nums2[temp_iter] = temp
                        if temp_iter<n-1:
                            temp_iter = temp_iter +1
                        else:
                            break
             
s = Solution()
s.merge([4,5,6,0,0,0]
,3,[1,2,3],3)