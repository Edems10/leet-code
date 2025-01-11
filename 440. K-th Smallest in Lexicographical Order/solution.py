

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        numbers_gen = []
        for i in range(1, n + 1):
            numbers_gen.append(str(i))
        numbers_gen.sort()
        for i in range(len(numbers_gen)):
            numbers_gen[i] = int(numbers_gen[i])
        return numbers_gen[k - 1]


def main():
    sol = Solution()
    print(sol.findKthNumber(1, 1))


if __name__ == "__main__":
    main()
