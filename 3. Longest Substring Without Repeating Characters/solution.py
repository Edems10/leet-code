class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        dict_checker = []
        max_local = 0
        max_global = 0
        iter = 0
        substring_begin = 0
        word_length = len(s)
        while iter < word_length:

            current_char = s[iter]
            if current_char not in dict_checker:
                iter += 1
                dict_checker.append(current_char)
                max_local += 1
                if max_global < max_local:
                    max_global = max_local
            else:
                substring_begin += 1
                remaining = substring_begin - word_length
                if remaining >= word_length - max_global:
                    break
                dict_checker.clear()
                max_local = 0
                iter = substring_begin
        return max_global


s = Solution()

print(s.lengthOfLongestSubstring("dvdf"))
