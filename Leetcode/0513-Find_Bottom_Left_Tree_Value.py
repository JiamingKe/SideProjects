# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        currentRow = []
        nextRow = [root]
        
        while len(nextRow) != 0:
            currentRow = nextRow
            nextRow = []
            for node in currentRow:
                if node.left is not None:
                    nextRow.append(node.left)
                if node.right is not None:
                    nextRow.append(node.right)
                    
        return currentRow[0].val

