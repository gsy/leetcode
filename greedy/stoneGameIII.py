class Solution:
    def stoneGameIII(self, stoneValue):
        length = len(stoneValue)
        best = []

        for j in range(length - 1, -1, -1):
            if j == length - 1:
                best.append(1)
            elif j == length - 2:
                a = stoneValue[length - 2]
                b = stoneValue[length - 2] + stoneValue[length - 1]
                if a > b:
                    best.append(1)
                else:
                    best.append(2)
            else:
                a = stoneValue[j]
                b = stoneValue[j] + stoneValue[j+1]
                c = stoneValue[j] + stoneValue[j+1] + stoneValue[j+2]
                maximum = max(a, b, c)
                if a == maximum:
                    best.append(1)
                elif b == maximum:
                    best.append(2)
                else:
                    best.append(3)

        i, j = 0, 0
        best = best[::-1]
        print(best)
        alice, bob = 0, 0
        turn = "alice"
        while i < length and j < length:
            if turn == "alice":
                steps = best[i]
                for k in range(steps):
                    alice += stoneValue[i+k]
                j = i + steps
                turn = "bob"
                continue

            if turn == "bob":
                steps = best[j]
                for k in range(steps):
                    bob += stoneValue[j+k]
                i = j + steps
                turn = "alice"

        if alice > bob:
            return "Alice"
        elif alice < bob:
            return "Bob"
        return "Tie"
