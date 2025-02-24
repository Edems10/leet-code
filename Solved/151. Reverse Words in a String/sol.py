class Solution:
    def reverseWords(self, s: str) -> str:
        split = s.split()
        reversed = split[::-1]
        string_reversed = ""
        for i in range(len(reversed)):
            if i == len(reversed) - 1:
                string_reversed += reversed[i]
            else:
                string_reversed += reversed[i] + " "
        return string_reversed


def main():
    s = Solution()
    print(s.reverseWords("  hello world  "))


if __name__ == "__main__":
    main()
