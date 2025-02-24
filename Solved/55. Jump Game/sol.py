from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, num in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + num)
        return True


if __name__ == "__main__":
    nums = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]
    print(Solution().canJump(nums))
