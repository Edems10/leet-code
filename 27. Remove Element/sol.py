from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return
        pointer_left = 0
        pointer_right = len(nums)-1
        
        added_underscore = 0
        while(pointer_left<=pointer_right):
            while(nums[pointer_left]==val):
                if pointer_left>pointer_right:
                    break
                nums[pointer_left] = nums[pointer_right]
                nums[pointer_right] = '_'
                added_underscore = added_underscore +1
                pointer_right = pointer_right -1
            pointer_left = pointer_left +1
        return len(nums)-added_underscore
        
if __name__ =="__main__":
    s = Solution()
    print(s.removeElement([1],1))
            