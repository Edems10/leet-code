from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            if nums[i] != 0:
                for j in range(0, i):
                    if nums[j] == 0:
                        nums[j] = nums[i]
                        nums[i] = 0
                        break


s = Solution()
print(s.moveZeroes([4, 2, 4, 0, 0, 3, 0, 5, 1, 0]))
