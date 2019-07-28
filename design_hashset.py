# -*- coding: utf-8 -*-

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = [None] * 10

    def add(self, key):
        while len(self.buckets) <= key:
            self.buckets = self.buckets + [None] * len(self.buckets)
        self.buckets[key] = key

    def remove(self, key: int) -> None:
        if key < len(self.buckets):
            self.buckets[key] = None


    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key < len(self.buckets):
            return self.buckets[key] is not None
        return False


if __name__ == "__main__":
    obj = MyHashSet()
    obj.add(1)
    obj.add(2)
    r = obj.contains(1)
    assert r is True
    r = obj.contains(3)
    assert r is False
    obj.add(2)
    r = obj.contains(2)
    assert r is True

    obj.remove(2)
    r = obj.contains(2)
    assert r is False
