from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = set()
        final_length = len(nums)
        i = 0
        while(i<len(nums)):
            if nums[i] in unique:
                nums.pop(i)
            else:
                unique.add(nums[i])
                i=i+1
        
        final_unique_length = len(nums)
        for _ in range(final_length-final_unique_length):
            nums.append('_')
        return final_unique_length
        

if __name__ =="__main__":
    s = Solution()
    s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])