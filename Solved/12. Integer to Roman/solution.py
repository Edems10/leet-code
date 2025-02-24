roman_hmap = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500: "D",
    900: "CM",
    1000: "M",
}


class Solution:
    def intToRoman(self, num: int) -> str:
        roman_translate = ""
        while num != 0:
            for number, roman in reversed(roman_hmap.items()):
                current_num = num
                current_roman = ""
                while True:
                    current_num = current_num - number
                    if current_num >= 0:
                        num = num - number
                        current_roman = current_roman + roman
                    else:
                        break
                roman_translate = roman_translate + current_roman
                if num == 0:
                    break
        return roman_translate


tests = [3749, 58, 1994]
s = Solution()
for test in tests:
    print(f"number {test} = {s.intToRoman(num=test)}")
