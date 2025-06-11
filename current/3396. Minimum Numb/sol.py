from collections import deque
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        nums_set = set(nums)
        nums = deque(nums)
        while len(nums)>len(nums_set):
            count +=1
            for _ in range(3):
                if not nums:
                    break
                nums.popleft()
            nums_set = set(nums)
            
        return count
    
s = Solution()
s.minimumOperations([1,2,3,4,2,3,3,5,7])