# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        currentRow = [root]
        ans = []
        while len(currentRow) != 0:
            nextRow = []
            currentMax = currentRow[0].val
            for node in currentRow:
                if node.left is not None:
                    nextRow.append(node.left)
                if node.right is not None:
                    nextRow.append(node.right)
                    
                if node.val > currentMax:
                    currentMax = node.val
            
            ans.append(currentMax)
            currentRow = nextRow
        return ans

