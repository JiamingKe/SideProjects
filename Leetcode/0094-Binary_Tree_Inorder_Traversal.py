# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        Left = self.inorderTraversal(root.left)
        Right = self.inorderTraversal(root.right)
        return Left + [root.val] + Right

