class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        last_s = 0
        star_iterator = 0
        found = 0
        for patern_char_iterator in range(len(p)):
            if p[patern_char_iterator] == "*":
                star_iterator = patern_char_iterator
        iterator_p = star_iterator+1
        pattern_length = len(p)- iterator_p
        if iterator_p>= len(p):
            return True
        while(iterator_p<len(p) and last_s<len(s)):
            if p[iterator_p] == ".":
                last_s +=1
                iterator_p +=1
                found += 1
            if s[last_s] == p[iterator_p]:
                last_s+=1
                iterator_p+=1
                found += 1
            else:
                found = 0
                last_s +=1
            if found == pattern_length:
                return True
        return False
            

sol= Solution()
s = "ab"
p = ".*"
sad=sol.isMatch(s,p)        
print(sad)    