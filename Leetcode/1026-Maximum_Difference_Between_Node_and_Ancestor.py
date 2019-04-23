# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        return self.computeDiff(root, [])
        
    def computeDiff(self, root: TreeNode, ancestors: List[int]) -> int:
        maxdiff = 0
        for val in ancestors:
            if abs(val- root.val) > maxdiff:
                maxdiff = abs(val- root.val)
                
        Left = 0
        if root.left is not None:
            Left = self.computeDiff(root.left, ancestors+[root.val])
        Right = 0
        if root.right is not None:
            Right = self.computeDiff(root.right, ancestors+[root.val])
        return max([Left, Right, maxdiff])
