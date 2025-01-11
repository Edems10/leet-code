class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if ransomNote == "":
            return True
        if magazine == "" and len(magazine) < len(ransomNote):
            return False
        
        ransom_dict = {}
        for char in magazine:
            ransom_dict[char] = ransom_dict.get(char, 0) + 1
        
        for char in ransomNote:
            if char in ransom_dict:
                ransom_dict[char] -= 1
                if ransom_dict[char] < 0:
                    return False
            else:
                return False
        return True
        
sol = Solution()
print(sol.canConstruct("aa", "aab"))