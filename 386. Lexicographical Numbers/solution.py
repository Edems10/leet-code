
from typing import List


class Solution:
    def lexicalOrder(self, n:int) -> List[int]:
        numbers_gen = []
        for i in range(1,n+1):
            numbers_gen.append(str(i))
        numbers_gen.sort()
        for i in range(len(numbers_gen)):
            numbers_gen[i]=int(numbers_gen[i])
        return(numbers_gen)
    
    
    
    
    
    
def main():
    sol = Solution()
    print(sol.lexicalOrder(13))
    
if __name__ =="__main__":
    main()