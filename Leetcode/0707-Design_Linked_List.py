class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= len(self.data):
            return -1
        return self.data[index]

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.data = [val] + self.data

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.data.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0:
            self.addAtHead(val)
            
        if index >= 0 and index <= len(self.data):
            self.addAtTail(val)
            self.data[index+1:] = self.data[index:-1]
            self.data[index] = val

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= 0 and index < len(self.data):
            self.data[index:-1] = self.data[index+1:]
            self.data = self.data[:-1]


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
