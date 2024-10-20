from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        found_dict = {}
        i = 0
        dup_removed = 0
        while i < len(nums):
            if nums[i] == None:
                break
            found = found_dict.get(nums[i])
            if found == 1:
                found_dict[nums[i]] = found + 1
                i = i + 1
            elif found == None:
                found_dict[nums[i]] = 1
                i = i + 1
            elif found == 2:
                nums.pop(i)
                nums.append(None)
                dup_removed = dup_removed + 1
        return len(nums) - dup_removed


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates([1, 1, 1, 2, 2, 3]))
