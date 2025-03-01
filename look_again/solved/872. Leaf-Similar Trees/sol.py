# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leafs(root: Optional[TreeNode]) -> Optional[list[int]]:
            if not root:
                return None

            leaf_values = []
            stack = deque([root])

            while stack:
                node = stack.pop()
                if not node.left and not node.right:
                    leaf_values.append(node.val)

                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            return leaf_values

        return leafs(root1) == leafs(root2)


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    s = Solution()
    s.leafSimilar(root1=root, root2=root)
