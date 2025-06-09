class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divisible,indivisible = [],[]
        for num in range(1,n+1):
            if (num % m) != 0:
                indivisible.append(num)
            else:
                divisible.append(num)
        
        return sum(indivisible)-sum(divisible)


s = Solution()
print(s.differenceOfSums(10,3))