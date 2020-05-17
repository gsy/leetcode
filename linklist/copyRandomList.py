#!/usr/bin/env python3

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def indexof(self, head, node):
        current = head
        index = 0
        while current:
            if current == node:
                return index
            else:
                current = current.next
                index += 1

    def get(self, head, index):
        current = head
        for i in range(index):
            current = current.next
        return current
               
    def copyRandomList(self, head):
        if head is None:
            return None

        copy = Node(0)

        node, prev = head, copy
        while node:
            newNode = Node(node.val, None, None)
            prev.next = newNode
            prev = newNode
            node = node.next

        node, prev = head, copy
        while node:
            current = prev.next
            if node.random is None:
                current.random = None
            elif node.random == node:
                current.random = current
            else:
                index = self.indexof(head, node.random)
                current.random = self.get(copy.next, index)

            node = node.next
            prev = current

        return copy.next
