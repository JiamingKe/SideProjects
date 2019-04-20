# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        array = self.toArray(head)
        stack = []
        for i in range(len(array)-1, -1, -1):
            if len(stack) == 0:
                stack.append(array[i])
                array[i] = 0
                continue
            
            temp = stack.pop()
            while len(stack) > 0 and temp <= array[i]:
                temp = stack.pop()
            
            if temp <= array[i]:
                stack.append(array[i])
                array[i] = 0
            else:
                stack.append(temp)
                stack.append(array[i])
                array[i] = temp
                
        return array
    
    def toArray(self, head: ListNode) -> List[int]:
        array = []
        while head is not None:
            array.append(head.val)
            head = head.next
        return array

