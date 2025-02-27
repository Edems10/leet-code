class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = ""
        for iter in range(max(len(word1), len(word2))):
            if iter < len(word1):
                merged_string += word1[iter]
            if iter < len(word2):
                merged_string += word2[iter]
        return merged_string
