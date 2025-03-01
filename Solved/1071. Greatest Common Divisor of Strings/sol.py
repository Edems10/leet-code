class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = ""
        current_prefix = ""

        def is_divisible(prefix, str: str):
            prefix_len = len(prefix)
            for i in range(0, len(str), prefix_len):
                if prefix != str[i : prefix_len + i]:
                    return False
            return True

        for char1, char2 in zip(str1, str2):
            if char1 == char2:
                current_prefix += char1
                if len(current_prefix) < len(gcd):
                    continue
                if is_divisible(current_prefix, str1) and is_divisible(
                    current_prefix, str2
                ):
                    gcd = current_prefix
            else:
                current_prefix = ""
        return str(gcd)


def main():
    str1 = "ABCABC"
    str2 = "ABC"
    solution = Solution()
    outcome = solution.gcdOfStrings(str1, str2)
    print(outcome)


if __name__ == "__main__":
    main()
