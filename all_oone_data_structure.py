# -*- coding: utf-8 -*-


class LinkNode(object):
    def __init__(self, data):
        self.value = data
        self.next = None


class LinkList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        node = LinkNode(value)
        if self.head is None:
            self.head = node
        if self.tail is None:
            self.tail = node
        else:
            node.next = self.head.next
            self.head.next = node
        if self.tail == self.head:
            self.tail = node

        return node

    def pop(self):
        self.head = self.head.next

    def __repr__(self):
        result = ""
        if self.head is not None:
            result += self.head.value
            next = self.head.next
            while next is not None:
                result = result + "->" + next.value
                next = next.next
        return result


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_value = {}
        self.keys = LinkList()
        self.nodes = {}
        self._max = None
        self._min = None

    def refresh_maximum(self, key, value):
        if self._max is None:
            self._max = value
            return True
        else:
            if value >= self._max:
                self._max = value
                return True
        return False

    def refresh_minimum(self, key, value):
        if value <= 0:
            return False

        if self._min is None:
            self._min = value
            return True
        else:
            if value <= self._min:
                self._min = value
                return True
        return False

    def find_node_by(self, key):
        return self.nodes[key]

    def swap_to_tail(self, key):
        node = self.find_node_by(key)
        self.keys.tail.value, node.value = node.value, self.keys.tail.value

    def swap_to_head(self, key):
        node = self.find_node_by(key)
        self.keys.head.value, node.value = node.value, self.keys.head.value

    def pop_head(self):
        self.keys.pop()

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.key_value:
            value = 1
            self.key_value[key] = value
            node = self.keys.insert(key)
            self.nodes[key] = node
        else:
            value = self.key_value[key] + 1
            self.key_value[key] = value

        update_maximum = self.refresh_maximum(key, value)
        self.refresh_minimum(key, value)
        if update_maximum:
            self.swap_to_tail(key)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.key_value:
            return

        value = self.key_value[key] - 1
        self.key_value[key] = value
        self.refresh_maximum(key, value)
        update_minimum = self.refresh_minimum(key, value)

        if value <= 0:
            del self.key_value[key]
            # 需要把这个值删掉
            node = self.find_node_by(key)
            if self.keys.head == node:
                self.keys.pop()

        if update_minimum:
            self.swap_to_head(key)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if self.keys.tail is not None:
            return self.keys.tail.value
        return ""

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self.keys.head is not None:
            return self.keys.head.value
        return ""
