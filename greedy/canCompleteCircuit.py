class Solution:
    def canCompleteCircuit(self, gas, cost):
        length = len(gas)
        result = 0
        total, current = 0, 0
        minimum = None

        for i in range(length):
            current += gas[i] - cost[i]
            total += gas[i] - cost[i]

            if minimum is None or current < minimum:
                minimum = current
                result = (i + 1) % length

        if total >= 0:
            return result

        return -1
