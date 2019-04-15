# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if root.val == sum and root.left is None and root.right is None:
            return True
        
        Left = False
        if root.left is not None:
            Left = self.hasPathSum(root.left, sum-root.val)
        
        Right = False
        if root.right is not None:
            Right = self.hasPathSum(root.right, sum-root.val)
            
        return Left or Right

