from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 0:
            return 0
        if len(ratings) == 1:
            return 1
        candy_distribution = 1
        ratings.sort()
        last_rating = ratings[0]
        all_candies = 1
        for rating in ratings[1::]:
            if rating != last_rating:
                candy_distribution += 1
            all_candies += candy_distribution
            last_rating = rating
        return all_candies


def main():
    s = Solution()
    print(s.candy([1, 2, 2]))


if __name__ == "__main__":
    main()
