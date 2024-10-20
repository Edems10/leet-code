from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        p_left = 0
        p_left_val = 0
        p_right = len(height) - 1
        p_right_val = 0
        max_water = 0
        while p_left != p_right:
            p_left_val = height[p_left]
            p_right_val = height[p_right]
            length = p_right - p_left
            if p_left_val >= p_right_val:
                p_right -= 1
                current = p_right_val * length
            else:
                p_left += 1
                current = p_left_val * length
            if current > max_water:
                max_water = current
        return max_water


s = Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(s)
