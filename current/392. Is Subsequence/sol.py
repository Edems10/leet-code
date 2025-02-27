class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        current_letter_t = 0
        for letter_s in s:
            for letter_t_iter in range(current_letter_t, len(t)):
                if letter_s is t[letter_t_iter]:
                    current_letter_t = letter_t_iter + 1
                    break
            else:
                return False
        return True


sol = Solution()
sol.isSubsequence("aaaaaa", "bbaaaa")
