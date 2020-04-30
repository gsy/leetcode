class Solution:
    def findRestaurant(self, list1, list2):
        index1 = {name: i for i, name in enumerate(list1)}

        result = []
        mini = None
        for j, name in enumerate(list2):
            if name in index1:
                current = index1[name] + j
                if mini is None or current < mini:
                    mini = current
                    result = [name]
                elif current == mini:
                    result.append(name)
        return result
