from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_height = 0
        max_height = 0
        for single_gain in gain:
            current_height += single_gain
            if current_height > max_height:
                max_height = current_height
        return max_height


if __name__ == "__main__":
    sol = Solution()
    print(sol.largestAltitude([-5, 1, 5, 0, -7]))
