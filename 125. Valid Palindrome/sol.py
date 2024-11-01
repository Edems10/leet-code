import re


class Solution:
    def remove_non_alphanumeric(self, s):
        return re.sub(r"[^a-zA-Z0-9]", "", s)

    def isPalindrome(self, s: str) -> bool:
        cleaned_string = self.remove_non_alphanumeric(s).lower()
        l = 0
        r = len(cleaned_string) - 1
        while l < r:
            if cleaned_string[l] != cleaned_string[r]:
                return False
            l = l + 1
            r = r - 1
        return True


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
