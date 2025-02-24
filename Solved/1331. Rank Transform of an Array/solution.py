from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unique_elements = set(arr)
        sorted_unique = sorted(unique_elements)

        rank_dict = {}
        for rank, num in enumerate(sorted_unique):
            rank_dict[num] = rank + 1

        ranked_array = []
        for numb in arr:
            ranked_array.append(rank_dict.get(numb))

        return ranked_array


s = Solution()
print(s.arrayRankTransform([40, 10, 20, 30]))
