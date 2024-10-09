from typing import List


class Solution:

    def arrayToHash(self, arr1: List[int]) -> dict:
        final_hash = {}
        for number in arr1:
            string_number = str(number)
            current_number = ""
            for i, num_char in enumerate(string_number):
                current_number += num_char
                final_hash[current_number] = i + 1
        return final_hash

    def findlongestPrefix(self, b_dict: dict, s_dict: dict) -> int:
        highest_val = 0
        for num in b_dict.keys():
            found = s_dict.get(num)
            if found and highest_val < found:
                highest_val = found
        return highest_val

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        data_1_hash = self.arrayToHash(arr1)
        data_2_hash = self.arrayToHash(arr2)

        if len(data_1_hash) >= len(data_2_hash):
            return self.findlongestPrefix(data_1_hash, data_2_hash)
        else:
            return self.findlongestPrefix(data_2_hash, data_1_hash)


def main():
    s = Solution()
    print(s.longestCommonPrefix([1, 2, 3], [4, 4, 4]))


if __name__ == "__main__":
    main()
