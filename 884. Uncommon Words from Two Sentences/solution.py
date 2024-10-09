from typing import List


class Solution:

    def appendIfUnique(self, word_dict: dict, word: str):
        word_exists = word_dict.get(word)
        if word_exists:
            word_dict[word] = word_exists + 1
        else:
            word_dict[word] = 1
        return word_dict

    def findwords(self, s1: str, word_dict: dict = None) -> dict:
        if word_dict == None:
            word_dict = {}
        word = ""
        for char in s1:
            if char != " ":
                word = word + char
            else:
                word_dict = self.appendIfUnique(word_dict, word)
                word = ""
        word_dict = self.appendIfUnique(word_dict, word)
        return word_dict

    def findUnique(self, dict: dict) -> List[str]:
        unique_words = []
        for word, amount in dict.items():
            if amount == 1:
                if word in unique_words:
                    unique_words.remove(word)
                else:
                    unique_words.append(word)
        return unique_words

    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        dict = self.findwords(s1)
        dict = self.findwords(s2, dict)
        unique_words = self.findUnique(dict)
        return unique_words


def main():
    tests = ["xf tyl xf", "gw p gw xf"]
    s = Solution()
    for i in range(0, len(tests), 2):
        print(s.uncommonFromSentences(tests[i], tests[i + 1]))


if __name__ == "__main__":

    # Auto-generated code below aims at helping you parse
    # the standard input according to the problem statement.

    while True:
        highest_mountain = 0
        highest_mountain_index = -1
        remaining_mountains = 8
        for i in range(remaining_mountains):
            mountain_h = int(input())  # represents the height of one mountain.
            if mountain_h > highest_mountain:
                highest_mountain_index = i
                highest_mountain = mountain_h
        print(highest_mountain)
        remaining_mountains -= remaining_mountains
