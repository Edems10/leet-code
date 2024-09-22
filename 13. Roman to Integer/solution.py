roman_hmap= {
    'I':    1,
    'V':    5,
    'X':    10,
    'L':    50,
    'C':    100,
    'D':    500,
    'M':    1000
}


roman_hmap_extra= {
    'IV':   4,
    'IX':   9,
    'XL':   40,
    'CD':   400,
    'XC':   90,
    'CM':   900
}


class Solution:
    def romanToInt(self,s: str)->int:
        number = 0
        found_two = False
        for char in range(len(s)):
            if found_two is True:
                found_two = False
                continue
            if char+1< len(s):
                two = s[char]+s[char+1]
                number_extra = roman_hmap_extra.get(two)
                if number_extra is not None:
                    number += number_extra
                    found_two = True
                    continue    
            number += roman_hmap.get(s[char])
        return number
            

def main():
    s = Solution()
    print(s.romanToInt("MCMXCIV"))
    
if __name__ =="__main__":
    main()