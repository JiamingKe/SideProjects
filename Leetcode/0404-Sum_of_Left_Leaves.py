# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        Left = 0
        if root.left is not None:
            if root.left.left is None and root.left.right is None:
                Left = root.left.val
            else:
                Left = self.sumOfLeftLeaves(root.left)
        Right = 0
        if root.right is not None:
            Right = self.sumOfLeftLeaves(root.right)
        return Left + Right
