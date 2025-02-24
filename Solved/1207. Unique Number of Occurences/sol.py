from typing import List


class Solution:
    def __init__(self):
        pass
    def uniqueOccurrences(self,arr:List[int])->bool:
        occurences = {}
        for number in arr:
            current_occurence = occurences.get(number)
            if current_occurence:
                occurences[number] = current_occurence +1
            else:
                occurences[number] = 1
        
        if len(occurences)!= len(set(occurences.values())):
            return False
        return True
        
        

def main():
    sol = Solution()
    print(sol.uniqueOccurences([1,2,2,2,1,1,3]))
    
if __name__ == "__main__":
    main()