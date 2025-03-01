from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        placable = 0
        iterator = 0
        len_flowerbed = len(flowerbed)

        def get_next_flower(flowerbed, iterator, len_flowerbed) -> int:
            if iterator + 1 >= len_flowerbed:
                return 0
            else:
                return flowerbed[iterator + 1]

        def get_previouse_flower(flowerbed, iterator):
            if iterator == 0:
                return 0
            else:
                return flowerbed[iterator - 1]

        def is_empty_spot(flowerbed, flower_position) -> bool:
            if flowerbed[flower_position] == 0:
                return True
            return False

        def move_to_next(number, iterator, len_flowerbed) -> [bool, int]:
            iterator += number
            if iterator >= len_flowerbed:
                return True, iterator
            return False, iterator

        while iterator <= len_flowerbed:
            plantable = is_empty_spot(flowerbed, iterator)
            if not plantable:
                overflow, iterator = move_to_next(2, iterator, len_flowerbed)
                if overflow:
                    break
                else:
                    continue

            next_flower = get_next_flower(flowerbed, iterator, len_flowerbed)
            previouse_flower = get_previouse_flower(flowerbed, iterator)
            overflow, iterator = move_to_next(1, iterator, len_flowerbed)

            if previouse_flower == 0 and next_flower == 0:
                placable += 1
                if placable == n:
                    return True
                overflow, iterator = move_to_next(1, iterator, len_flowerbed)
                if overflow:
                    break

        return False


if __name__ == "__main__":
    s = Solution()
    outcome = s.canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2)
    print(outcome)
