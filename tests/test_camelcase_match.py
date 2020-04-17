# -*- coding: utf-8 -*-

from camelcase_match import Solution


if __name__ == '__main__':
    s = Solution()
    queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
    pattern = "FB"
    r = s.camelMatch(queries, pattern)
    print(r)

    queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
    pattern = "FoBa"
    r = s.camelMatch(queries, pattern)
    print(r)

    queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
    pattern = "FoBaT"
    r = s.camelMatch(queries, pattern)
    print(r)
