# -*- coding: utf-8 -*-

class Solution:
    def build_index(self, ls):
        index = {}
        for i, item in enumerate(ls):
            index[item] = i
        return index

    def findRestaurant(self, list1, list2):
        index1 = self.build_index(list1)
        index2 = self.build_index(list2)

        total, result = None, []
        for key in index1:
            if key in index2:
                current = index1[key] + index2[key]
                if total is None:
                    total = current
                    result = [key]
                else:
                    if current < total:
                        result = [key]
                        total = current
                    elif current == total:
                        result.append(key)
        return result

if __name__ == "__main__":
    s = Solution()
    r = s.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"])
    assert r == ["Shogun"]

    r = s.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"])
    assert r == ["Shogun"]
