class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = [-1] * 10
        self.length = len(self.buckets)


    def put(self, key, value):
        """
        value will always be non-negative.
        """
        while len(self.buckets) <= key:
            self.buckets = self.buckets + [-1] * len(self.buckets)
            self.length = self.length * 2
        self.buckets[key] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key < self.length:
            return self.buckets[key]
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key < self.length:
            self.buckets[key] = -1


if __name__ == "__main__":
    obj = MyHashMap()
    obj.put(1, 1)
    obj.put(2, 2)
    r = obj.get(1)
    assert r == 1

    r = obj.get(3)
    assert r == -1

    obj.put(2, 1)
    r = obj.get(2)
    assert r == 1

    obj.remove(2)
    r = obj.get(2)
    assert r == -1
