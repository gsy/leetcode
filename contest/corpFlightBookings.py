class Solution:
    def corpFlightBookings(self, bookings, n):
        bookings = sorted(bookings, key=lambda item: item[0])

        delta = [0] * (n + 1)
        for ls in bookings:
            start, end, count = ls
            delta[start] = delta[start] + count
            if end + 1 < n + 1:
                delta[end+1] = delta[end+1] - count

        result = []
        prev = 0
        for i in range(1, n+1):
            tmp = delta[i] + prev
            result.append(tmp)
            prev = tmp

        return result
