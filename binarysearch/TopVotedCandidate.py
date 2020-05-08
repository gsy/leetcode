class TopVotedCandidate:

    def __init__(self, persons, times):
        self.persons = persons
        self.lenp = len(persons)
        self.times = times
        self.lent = len(times)
        self.winners = self.whoWins()

    def whoWins(self):
        votes = {}
        maximum = None
        winners = []
        winner = None
        for i, person in enumerate(self.persons):
            votes[person] = votes.get(person, 0) + 1
            if maximum is None or votes[person] >= maximum:
                winner = person
                maximum = votes[person]
                winners.append(winner)
            else:
                winners.append(winner)
        return winners

    def q(self, t: int) -> int:
        left, right = 0, self.lent - 1

        end = 0
        found = False
        while left < right:
            mid = (left + right + 1) // 2

            if self.times[mid] == t:
                end = mid
                found = True
                break
            elif self.times[mid] > t:
                right = mid - 1
            else:
                left = mid

        if found is False:
            end = left
        # print("end", end)

        return self.winners[end]



if __name__ == "__main__":
    persons = [0, 1, 1, 0, 0, 1, 0]
    times = [0, 5, 10, 15, 20, 25, 30]

    obj = TopVotedCandidate(persons, times)
    r1 = obj.q(3)
    print(r1)

    r2 = obj.q(12)
    print(r2)

    r3 = obj.q(25)
    print(r3)

    r4 = obj.q(15)
    print(r4)

    r5 = obj.q(24)
    print(r5)

    r6 = obj.q(8)
    print(r6)


