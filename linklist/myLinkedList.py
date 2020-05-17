#!/usr/bin/env python3

class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = LinkNode(0)
        self.tail = self.head
        self.length = 0


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.length:
            return -1

        node = self.head.next
        for i in range(index):
            node = node.next

        return node.val


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = LinkNode(val)
        node.next = self.head.next
        self.head.next = node
        self.length = self.length + 1

        if self.length == 1:
            self.tail = node


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = LinkNode(val)
        self.tail.next = node
        self.tail = node
        self.length = self.length + 1


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.length:
            return
        elif index == self.length:
            self.addAtTail(val)
        else:
            prev = self.head
            node = self.head.next
            for i in range(index):
                prev = prev.next
                node = node.next

            prev.next = LinkNode(val)
            prev.next.next = node
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.length:
            return

        prev = self.head
        node = prev.next
        for i in range(index):
            prev = prev.next
            node = node.next

        prev.next = node.next
        node = None

        if index == self.length - 1:
            self.tail = prev

        self.length -= 1



# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
a = obj.get(0)
print(a)

obj.addAtHead(1)
print(obj.get(0))

obj.addAtTail(3)
print(obj.get(0), obj.get(1))

obj.addAtIndex(1, 2)
print(obj.get(0), obj.get(1), obj.get(2))

obj.deleteAtIndex(3)
print(obj.get(0), obj.get(1))
