class Solution:
    
    vowels = {"a","A","e","E","i","I","o","O","u","U"}
    def reverseVowels(self, s: str) -> str:
        positions = []
        s_list = list(s)
        for iterator in range(len(s)):
            if s[iterator] in self.vowels:
                positions.append(iterator)
        if len(positions)<=1:
            return s
        beggining = 0
        end = len(positions) -1
        while beggining<end:
            s_list[positions[beggining]] = s[positions[end]]
            s_list[positions[end]]= s[positions[beggining]]
            beggining +=1
            end -=1
        return ''.join(s_list)            
            
            
        
s = Solution()
s.reverseVowels("IceCreAm") 