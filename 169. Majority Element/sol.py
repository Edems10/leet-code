from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements_appeared = {}
        for num in nums:
            appeared = elements_appeared.get(num)
            if appeared:
                appeared = appeared + 1
                elements_appeared[num] = appeared
            else:
                elements_appeared[num] = 1
        return max(elements_appeared, key=elements_appeared.get)


if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([3, 3, 4]))
