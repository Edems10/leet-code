from typing import List


class Solution:
    # def findMaxAverage(self, nums: List[int], k: int) -> float:
    #     window = 0
    #     max_avg = None
    #     while window<=len(nums)-k:
    #         window_sum = 0
    #         for i in range(window,window+k,1):
    #             window_sum += nums[i]
    #         avg = window_sum/k
    #         window +=1
    #         if max_avg == None:
    #             max_avg = avg
    #         if avg > max_avg:
    #             max_avg = avg
    #     return max_avg

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == 0 or len(nums) == 0:
            return 0

        current_sum = sum(nums[:k])
        max_sum = current_sum
        for i in range(k, len(nums)):
            current_sum = current_sum - nums[i - k] + nums[i]
            max_sum = max(current_sum, max_sum)
        return max_sum / k


def main():
    nums = [-1]
    s = Solution()
    s.findMaxAverage(nums, 1)


if __name__ == "__main__":
    main()
