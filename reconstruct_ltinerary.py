__author__ = 'guang'

class Solution(object):
    def find_a_path(self, graph, station, result, length):
        """
        >>> s = Solution()
        >>> graph = {"A": ["B"], "B": ["C"], "C": ["D"]}
        >>> station = "A"
        >>> result = []
        >>> length = 3
        >>> s.find_a_path(graph, station, result, length)
        True
        >>> result
        ['A', 'B', 'C', 'D']
        >>> graph = {"A": ["B", "C"], "B": ["A", "C"], "C": ["A"]}
        >>> station = "A"
        >>> result = []
        >>> length = 5
        >>> s.find_a_path(graph, station, result, length)
        False
        >>> graph = {"A": ["B", "C"], "B": ["C"], "C": ["A", "B"]}
        >>> station = "A"
        >>> result = []
        >>> length = 5
        >>> s.find_a_path(graph, station, result, length)
        True
        >>> result
        ['A', 'B', 'C', 'A', 'C', 'B']
        """
        result.append(station)
        if len(result) == length + 1:
            return True

        candidates = graph[station] if station in graph else []
        for index, next_station in enumerate(candidates):
            graph[station].pop(index)
            if self.find_a_path(graph, next_station, result, length):
                return True
            result.pop()
            graph[station].insert(index, next_station)

        return False

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        >>> s = Solution()
        >>> tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        >>> s.findItinerary(tickets)
        ['JFK', 'MUC', 'LHR', 'SFO', 'SJC']
        >>> tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
        >>> s.findItinerary(tickets)
        ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']
        >>> tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
        >>> s.findItinerary(tickets)
        ['JFK', 'NRT', 'JFK', 'KUL']
        """
        if tickets == [[]] or not tickets:
            return []

        graph = {}
        for ticket in tickets:
            departure, destination = ticket[0], ticket[1]
            if departure in graph.keys():
                graph[departure].append(destination)
            else:
                graph[departure] = [destination]

        for key, value in graph.items():
            graph[key] = sorted(value)

        start = "JFK"
        result = []
        self.find_a_path(graph, start, result, len(tickets))
        return result

