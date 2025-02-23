from typing import List


class Solution:
    def get_seen_values(
        self, numbers: List[int], numbers2: List[int]
    ) -> dict[int, [int, int]]:
        seen = {}
        for number in numbers:
            if not seen.get(number):
                seen[number] = [1]
        for number in numbers2:
            if not seen.get(number):
                seen[number] = [2]
            else:
                if seen.get(number) == [1]:
                    seen[number] = [1, 2]
        return seen

    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        seen = self.get_seen_values(nums1, nums2)
        result_1 = []
        result_2 = []
        for key, value in seen.items():
            if value == [1]:
                result_1.append(key)
            if value == [2]:
                result_2.append(key)
        return [result_1, result_2]


if __name__ == "__main__":
    sol = Solution()
    sol.findDifference([1, 2, 3], [2, 4, 6])
