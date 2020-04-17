# -*- coding: utf-8 -*-

import heapq


class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        heap = []
        for key, value in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (value, key))
            else:
                if value > heap[0][0]:
                    heapq.heappushpop(heap, (value, key))
            # print(heap)
        return [item[1] for item in heap]


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    r = s.topKFrequent(nums, 2)
    print(r)
    assert r == [2, 1]

    r = s.topKFrequent(nums, 1)
    assert r == [1]

    r = s.topKFrequent([3, 0, 1, 0], 1)
    print(r)
    assert r == [0]
