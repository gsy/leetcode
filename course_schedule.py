class Solution(object):
    def detect_cycle(self, graph, course, explored):
        """
        >>> s = Solution()

        # >>> graph = {0: [1], 1:[0]}
        # >>> s.detect_cycle(graph, 0, [])
        # True
        # >>> s.detect_cycle(graph, 1, [])
        # True
        # >>> graph = {0:[1]}
        # >>> s.detect_cycle(graph, 0, [])
        # False
        # >>> s.detect_cycle(graph, 1, [])
        # False
        # >>> graph = {0:[1], 1:[2]}
        # >>> s.detect_cycle(graph, 0, [])
        # False
        # >>> s.detect_cycle(graph, 1, [0])
        # False
        # >>> s.detect_cycle(graph, 2, [0, 1])
        # False
        # >>> graph = {0:[1], 1:[2], 2:[0]}
        # >>> s.detect_cycle(graph, 0, [])
        # True
        # >>> graph = {1:[0], 2:[1], 3:[2], 4:[1], 5:[4]}
        # >>> s.detect_cycle(graph, 1, [])
        # False
        # >>> s.detect_cycle(graph, 4, [1])
        # False
        # >>> graph = {0:[1], 1:[2, 3, 4], 2:[4]}
        # >>> s.detect_cycle(graph, 0, [])
        # False
        # >>> s.detect_cycle(graph, 1, [0])
        # False
        # >>> graph = {0:[1], 1:[2], 2:[3], 3:[0]}
        # >>> s.detect_cycle(graph, 0, [])
        # True
        # >>> graph = {0:[1], 1:[2,3], 2:[5], 3:[4], 4:[5], 5:[6]}
        # >>> s.detect_cycle(graph, 0, [])
        # False

        >>> graph = {0:[1], 1:[2,3], 2:[5], 3:[4], 5:[6], 6:[4]}
        >>> s.detect_cycle(graph, 0, [])
        False
        """
        WHITE, GREY, BLACK = 0, 1, 2
        stack = [course]
        color_mapping = {}
        seen = []
        while stack:
            course = stack.pop()
            seen.append(course)

            if course not in graph or course in explored:
                continue

            if color_mapping[course] == GREY:
                color_mapping[course] = BLACK
            else:
                color_mapping[course] = GREY

            for vertex in graph[course]:
                stack.append(vertex)

        explored.extend(seen)
        return False

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        >>> s = Solution()
        >>> n, graph = 2, [[1,0]]
        >>> s.canFinish(n, graph)
        True
        >>> n, graph = 2, [[1,0], [0,1]]
        >>> s.canFinish(n, graph)
        False
        >>> n, graph = 3, [[1,0], [2,1]]
        >>> s.canFinish(n, graph)
        True
        >>> n, graph = 3, [[1,0], [2,1], [3,1]]
        >>> s.canFinish(n, graph)
        True
        >>> n, graph = 3, [[1,0], [2,1], [3,1]]
        >>> s.canFinish(n, graph)
        True
        >>> n, graph = 3, [[1,0], [2,1], [3,1], [4,2], [4,1]]
        >>> s.canFinish(n, graph)
        True
        >>> n, graph = 3, [[1,0], [2,1], [3,1], [4,3], [5,2], [1,4]]
        >>> s.canFinish(n, graph)
        False
        >>> n, graph = 3, [[1,0], [2,1], [3,1], [5, 2], [4,3],[5, 4]]
        >>> s.canFinish(n, graph)
        True
        """
        if len(prerequisites) <= 1:
            return True

        courses = [course for course in range(numCourses)]
        graph = {}
        for edge in prerequisites:
            course, prerequisite = edge
            if prerequisite in graph:
                graph[prerequisite].append(course)
            else:
                graph[prerequisite] = [course]

        explored = []
        for course in courses:
            if course not in explored and self.detect_cycle(graph, course, explored):
                return False

        return True
