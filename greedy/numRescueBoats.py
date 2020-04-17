class Solution:
    def search(self, limit, people):
        # maximum (p <= limit)
        length = len(people)
        if length == 0:
            return False, None
        if people[0] > limit:
            return False, None

        left, right = 0, length - 1
        while left < right:
            mid = (left + right) // 2
            if mid == left:
                break
            if people[mid] > limit:
                right = mid - 1
            elif people[mid] <= limit:
                left = mid

        return True, left

    def numRescueBoats(self, people, limit):
        people = sorted(people)
        count = 0
        ships = []
        length = len(people)
        rescured = 0

        while rescured < length:
            person = people.pop(-1)

            if person >= limit:
                rescured += 1
                count += 1
                ships.append(person)
            else:
                found, index = self.search(limit - person, people)
                # print(limit - person, people, found, index)
                if found:
                    b = people.pop(index)
                    rescured += 2
                    ships.append((person, b))
                else:
                    rescured += 1
                    ships.append(person)
                count += 1
            # print("ships", ships)
        return count
