class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


def main():
    s = Solution()
    print(s.lengthOfLastWord("Hello World"))
    print(s.lengthOfLastWord("   fly me   to   the moon  "))
    print(s.lengthOfLastWord("luffy is still joyboy"))


if __name__ == "__main__":
    main()
