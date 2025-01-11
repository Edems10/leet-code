from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = set()
        duplicates_found = 0
        i = 0
        while i < len(nums):
            if nums[i] is None:
                break
            if nums[i] in unique:
                nums.pop(i)
                nums.append(None)
                duplicates_found = duplicates_found + 1
            else:
                unique.add(nums[i])
                i = i + 1
        return len(nums) - duplicates_found


if __name__ == "__main__":
    s = Solution()
    s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
