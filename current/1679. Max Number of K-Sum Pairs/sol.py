from typing import List


class Solution:



    def maxOperations(self, nums: List[int], k: int) -> int:
        frequency_dict = {}
        for num in nums:
            frequency_dict[num] = frequency_dict.get(num, 0) + 1
        
        operations = 0
        for num in frequency_dict:
            complement = k - num
            
            if num == complement:
                operations += frequency_dict[num] // 2
            elif complement in frequency_dict and num < complement:  
                operations += min(frequency_dict[num], frequency_dict[complement])
        
        return operations



s =Solution()
s.maxOperations(nums = [3,1,3,4,3], k= 6)