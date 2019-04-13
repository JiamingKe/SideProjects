# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        arrays = self.convert(root)
        totalSum = 0
        for a in arrays:
            totalSum += self.compute(a)
        
        return totalSum
            
    def convert(self, root: TreeNode) -> list:
        if root.left is None and root.right is None:
            return [[root.val]]
        
        result = []
        if root.left is not None:
            temp = self.convert(root.left)
            for i in range(len(temp)):
                temp[i] = [root.val] + temp[i]
            result+= temp
        if root.right is not None:
            temp = self.convert(root.right)
            for i in range(len(temp)):
                temp[i] = [root.val] + temp[i]
            result+= temp
        
        return result
    
    def compute(self, A: list) -> int:
        decimal = 0
        for i in range(len(A)):
            if A[i] == 1:
                decimal += 2**(len(A[i:])-1)
        return decimal
