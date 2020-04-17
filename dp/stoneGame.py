class Solution:
    def stoneGameIII(self, stoneValue):
        length = len(stoneValue)
        alice, bob = 0, 0
        alice_total, bob_total = 0, 0

        turn = "alice"

        while True:
            if alice >= length or bob >= length:
                break

            if turn == "alice":
                tmp = 0
                local_max = None
                local_max_id = None

                for i in range(alice, min(alice+3, length)):
                    value = stoneValue[i]
                    tmp = tmp + value

                    if local_max is None:
                        local_max = tmp
                        local_max_id = i
                    elif tmp > local_max:
                        local_max = tmp
                        local_max_id = i

                if local_max:
                    alice_total = alice_total + local_max
                    bob = local_max_id + 1

                turn = "bob"

            if turn == "bob":
                tmp = 0
                local_max = None
                local_max_id = None

                for i in range(bob, min(bob+3, length)):
                    value = stoneValue[i]
                    tmp = tmp + value

                    if local_max is None:
                        local_max = tmp
                        local_max_id = i
                    elif tmp > local_max:
                        local_max = tmp
                        local_max_id = i

                if local_max:
                    bob_total = bob_total + local_max
                    alice = local_max_id + 1
                turn = "alice"

        print(alice_total, bob_total)
        if alice_total > bob_total:
            return "Alice"
        elif alice_total < bob_total:
            return "Bob"
        else:
            return "Tie"
