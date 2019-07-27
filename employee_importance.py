
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        # 广度遍历，找到所有的下属，然后加上重要性
        mapping = {}
        for employee in employees:
            mapping[employee.id] = employee

        ids = [id]
        total = 0
        while len(ids) > 0:
            current = mapping[ids.pop(0)]
            total = total + current.importance
            ids = ids + current.subordinates
        return total

if __name__ == "__main__":
    s = Solution()
    r = s.getImportance([Employee(1, 5, [2, 3]), Employee(2, 3, []), Employee(3, 3, [])], 1)
    assert r == 11

    r = s.getImportance([Employee(1, 15, [2]), Employee(2, 10, [3]), Employee(3, 5, [])], 1)
    assert r == 30
