from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        max_match = strs[0]
        for word in range(1, len(strs)):
            current_word = strs[word]
            len_current_word = len(current_word)
            if current_word == "":
                return ""
            current_max_match = ""
            for letter, letter_iter in zip(max_match, range(len(max_match))):
                if letter_iter < len_current_word:
                    if letter in current_word[letter_iter]:
                        current_max_match += letter
                    else:
                        break
                else:
                    break
            max_match = current_max_match
            if max_match == "":
                return ""
        return max_match


def main():
    tests = ["flower", "flow", "flight"]
    s = Solution()
    print(s.longestCommonPrefix(tests))


if __name__ == "__main__":
    main()
