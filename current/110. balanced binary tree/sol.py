# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def helper(self, root: Optional[TreeNode], curr: int) -> int:
        if not root:
            return curr
        left_height = self.helper(root.left, curr + 1)
        if left_height == -1:
            return -1
        right_height = self.helper(root.right, curr + 1)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height)
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.helper(root, 0) != -1