"""Module for solving Sorted array binary tree"""
from typing import List, Optional

class TreeNode:
    def __init__(self,val =0 , left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    def convertArrayToBST(self, start, end, nums)-> Optional[TreeNode]:
        if start > end:
            return None
        middle = (start+end)//2
        t = TreeNode(val =nums[middle])
        t.left = self.convertArrayToBST(start=start, end=middle-1, nums=nums)
        t.right = self.convertArrayToBST(start=middle+1, end=end, nums=nums)
        return t
        
    
    def sortedArrayToBST(self, nums : List[int]) -> Optional[TreeNode]:
        return self.convertArrayToBST(start=0, end=len(nums)-1, nums=nums)
            
            
            
        
    
def main():
    nums = [-10,-3,0,5,9]
    s = Solution()
    idk= s.sortedArrayToBST(nums)
    print(idk)
    
if __name__=="__main__":
    main()
        