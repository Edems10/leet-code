from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        return self.helper_triplets(nums, 0, float('inf'), float('inf'))

    def helper_triplets(self, nums: List[int], i: int, first: float, second: float) -> bool:
        if i >= len(nums):
            return False

        if nums[i] <= first:
            return self.helper_triplets(nums, i + 1, nums[i], second)
        elif nums[i] <= second:
            return self.helper_triplets(nums, i + 1, first, nums[i])
        else:
            return True



if __name__ == "__main__":
    nums = [1,5,0,4,1,3]
    s = Solution()
    res = s.increasingTriplet(nums)
    print(res)
