# encoding: utf-8
__author__ = 'guang'

class Heap(object):
    def __init__(self, sources):
        """
        根据数组创建最小堆，使用list作为最小堆的数据结构
        :return:
        >>> h = Heap([[1, 3, 7, 13], [2, 6, 9], [5, 11, 13], [7, 19, 21]])
        >>> h.list
        [None, None, None, 1, 2, 5, 7]
        >>> h = Heap([])
        >>> h.list
        []
        >>> h = Heap([[1]])
        >>> h.list
        [1]
        >>> h = Heap([[1], [2]])
        >>> h.list
        [None, 1, 2]
        >>> h = Heap([[1], [2], [3]])
        >>> h.list
        [None, None, None, 1, 2, 3]
        """
        self.list = []
        self.nodes = len(sources)

        self.jobs_done = 0
        n = 0
        capacity = 2 ** n
        while capacity < self.nodes:
            for count in range(capacity):
                self.list.append(None)

            n += 1
            capacity = 2 ** n

        for ls in sources:
            if len(ls) > 0:
                self.list.append(ls[0])
            else:
                self.list.append(None)

        self.sources = []
        for source in sources:
            g = (x for x in source)
            self.sources.append(g)

        for g in self.sources:
            g.next()

    def left(self, parent):
        """

        :param parent:
        :return:
        >>> h = Heap([[1], [2]])
        >>> h.left(0)
        1
        >>> h.left(1)

        >>> h.left(2)

        """
        if parent * 2 + 1 < len(self.list):
            return self.list[parent * 2 + 1]
        else:
            return None

    def right(self, parent):
        """
        :param parent:
        :return:
        >>> h = Heap([[1], [2]])
        >>> h.right(0)
        2
        >>> h.left(1)

        >>> h.left(2)

        """

        if parent * 2 + 2 < len(self.list):
            return self.list[parent * 2 + 2]
        else:
            return None

    def is_leaf(self, node):
        return node in range(self.nodes - 1, len(self.list))

    def minimum(self, left, right):
        if left is None and right is None:
            return "None", None
        elif left is None:
            return "right", right
        elif right is None:
            return "left", left
        else:
            if left < right:
                return "left", left
            else:
                return "right", right

    def heapify(self):
        """
        :return:
        >>> h = Heap([[1], [2], [5], [7]])
        >>> h.heapify()

        >>> h.list
        [None, 1, 5, None, 2, None, 7]
        >>> h.heapify()
        1
        >>> h.list
        [1, 2, 5, None, None, None, 7]
        >>> h.heapify()
        2
        >>> h.list
        [2, None, 5, None, None, None, 7]
        >>> h.heapify()
        5
        >>> h.list
        [5, None, 7, None, None, None, None]
        >>> h.heapify()
        7
        >>> h.list
        [7, None, None, None, None, None, None]
        """
        def helper(node):
            if node > len(self.list):
                return

            if self.is_leaf(node):
                self.list[node] = self.get(node)
                return

            left = self.left(node)
            right = self.right(node)
            side, value = self.minimum(left, right)

            self.list[node] = value
            left_node = node * 2 + 1
            right_node = node * 2 + 2

            if side == "left":
                helper(left_node)
            elif side == "right":
                helper(right_node)
            else:
                helper(left_node)
                helper(right_node)

        helper(0)
        return self.list[0]

    def get(self, node):
        offset = self.nodes - 1
        index = node - offset
        already_done = []
        try:
            return self.sources[index].next()
        except StopIteration:
            if index not in already_done:
                self.jobs_done += 1
            already_done.append(index)
            return None

    def sort(self):
        """
        :return:
        >>> sources = [[1, 3, 7, 13], [2, 6, 9], [5, 11, 13], [7, 19, 21]]
        >>> h = Heap(sources)
        >>> h.sort()
        [1, 2, 3, 5, 6, 7, 7, 9, 11, 13, 13, 19, 21]
        """
        result = []
        head = None
        while self.jobs_done < self.nodes:
            head = self.heapify()
            if head is not None:
                result.append(head)

        while head is not None:
            head = self.heapify()
            if head is not None:
                result.append(head)

        return result
