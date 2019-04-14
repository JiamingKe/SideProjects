"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        
        if len(root.children) == 0:
            return 1
        
        return max([self.maxDepth(c) for c in root.children])+1

