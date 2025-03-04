from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot = 0
        left_part = 0
        right_part = sum(nums[1 : len(nums)])
        if left_part == right_part:
            return pivot
        for pivot in range(1, len(nums)):
            left_part = left_part + nums[pivot - 1]
            right_part = right_part - nums[pivot]
            if left_part == right_part:
                return pivot
        return -1


s = Solution()
s.pivotIndex([1, 7, 3])
