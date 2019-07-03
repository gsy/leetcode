# -*- coding: utf-8 -*-

from game24 import Solution


if __name__ == '__main__':
    s = Solution()
    # result = s.get_two_out_of([1, 2, 3, 4])
    # for x in result:
    #     print(x)

    result = s.judgePoint24([4, 1, 8, 7])
    print(result)
    assert result is True

    result = s.judgePoint24([2, 2, 3, 3])
    print(result)
    assert result is True

    result = s.judgePoint24([1, 2, 4, 6])
    print(result)
    assert result is True

    result = s.judgePoint24([1, 24, 2, 2])
    print(result)
    assert result is True

    result = s.judgePoint24([1, 2, 1, 2])
    print(result)
    assert result is False

    result = s.judgePoint24([3, 3, 8, 8])
    print(result)
    assert result is True

    result = s.judgePoint24([3, 4, 6, 7])
    print(result)
    assert result is False
