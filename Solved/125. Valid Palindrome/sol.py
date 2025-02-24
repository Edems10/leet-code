import re


class Solution:
    def remove_non_alphanumeric(self, s):
        return re.sub(r"[^a-zA-Z0-9]", "", s)

    def isPalindrome(self, s: str) -> bool:
        cleaned_string = self.remove_non_alphanumeric(s).lower()
        left = 0
        right = len(cleaned_string) - 1
        while left < right:
            if cleaned_string[left] != cleaned_string[right]:
                return False
            left = left + 1
            right = right - 1
        return True


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
