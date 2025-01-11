from typing import List

keyboard = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


class Solution:

    def recursionletterHelper(self, digits: str, combinations=None):

        if digits == "":
            return combinations

        current_digit = digits[0]
        digits = digits[1:]
        current_combinations = combinations
        current_keyboard = keyboard.get(current_digit)
        if current_combinations is None:
            current_combinations = []
            for key in keyboard.get(current_digit):
                current_combinations.append(key)
            return self.recursionletterHelper(digits, current_combinations)

        final_combination = []
        for combination in current_combinations:
            new_combination_list = []
            for current_key in current_keyboard:
                new_combination_list.append(combination + current_key)
            for new_combination in new_combination_list:
                final_combination.append(new_combination)
        return self.recursionletterHelper(digits, final_combination)

    def letterCombination(self, digits: str) -> List[str]:
        return self.recursionletterHelper(digits)


tests = ["23", "", "2"]


def main():
    solution = Solution()
    for test in tests:
        print(f"solution for {test} is: {solution.letterCombination(test)}")


if __name__ == "__main__":
    main()
