# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        index = 0
        for i in range(1, len(preorder)):
            if preorder[i] > preorder[0]:
                index = i
                break
        
        if index == 0:
            index = len(preorder)
        
        root.left = self.bstFromPreorder(preorder[1:index])
        root.right = self.bstFromPreorder(preorder[index:])
            
        return root
