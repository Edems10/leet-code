from collections import deque


class Solution:
    def tribonacci(self, n: int) -> int:
        trib = deque([0, 1, 1])
        if n == 3:
            return 2
        if n == 1 or n == 2:
            return 1
        if n == 0:
            return 0

        for _ in range(3, n):
            trib.append(sum(trib))
            trib.popleft()
        return sum(trib)


s = Solution()
res = s.tribonacci(25)
print(f"{res=}")
