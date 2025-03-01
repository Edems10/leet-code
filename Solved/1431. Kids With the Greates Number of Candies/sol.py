from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies_before_inflation_hit = max(candies)
        soon_to_be_diabetic_kids = []
        for candy in candies:
            if candy + extraCandies >= max_candies_before_inflation_hit:
                soon_to_be_diabetic_kids.append(True)
            else:
                soon_to_be_diabetic_kids.append(False)

        return soon_to_be_diabetic_kids
