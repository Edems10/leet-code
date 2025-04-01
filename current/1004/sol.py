from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        fr = {}
        l =0
        r= 0
        max_size = 0
        while r<len(nums):
            fr[nums[r]]= fr.get(nums[r],0)+1
            
            if fr.get(0, 0) > k:
                while fr[0]>k:
                    fr[nums[l]] = fr[nums[l]]-1
                    l+=1
            max_size = max(r-l+1,max_size)
            r+=1
        return max_size
    
    
s = Solution()
s.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3)