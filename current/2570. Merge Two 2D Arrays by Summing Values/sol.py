from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = {}

        for id, val in nums1 + nums2:
            res[id] = res.get(id, 0) + val
        
        return sorted([[id, val] for id, val in res.items()])

    
    
nums1 = [[2,4],[3,6],[5,5]]
nums2 = [[1,3],[4,3]]

s = Solution()
s.mergeArrays(nums1,nums2)