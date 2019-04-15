# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        array = []
        while head is not None:
            array.append(head.val)
            head = head.next
        
        if len(array) < 2:
            return True
        
        temp = array[:int(len(array)/2)]
        if len(array)%2 == 0:
            return temp[::-1] == array[int(len(array)/2):]
        else:
            return temp[::-1] == array[int(len(array)/2+1):]
