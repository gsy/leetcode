# -*- coding: utf-8 -*-

from basic_calculator import Solution


if __name__ == '__main__':
    s = Solution()
    result = s.calculate("1 + 2")
    assert result == 3
    print(result)

    print("-" * 30)
    result = s.calculate("1 - 2")
    assert result == -1
    print(result)

    print("-" * 30)
    result = s.calculate("1 + 2 + 3 + 4")
    assert result == 10
    print(result)

    print("-" * 30)
    result = s.calculate("1 + (2 + 3) + 5")
    print(result)
    assert result == 11
    print(result)

    result = s.calculate("(1 + 2)")
    assert result == 3
    print(result)

    result = s.calculate("(1 + 2) + 3")
    assert result == 6
    print(result)

    result = s.calculate("(1 - 2) + 3 + (5 + 6)")
    print(result)
    assert result == 13

    result = s.calculate("3 + (1 - 2)")
    assert result == 2
    print(result)

    result = s.calculate("10 + 3")
    assert result == 13
    print(result)

    result = s.calculate("2147483647")
    assert result == 2147483647
    print(result)

    result = s.calculate(" 2-1 + 2")
    assert result == 3
    print(result)

    result = s.calculate("2-(5-6)")
    assert result == 3
    print(result)

    print("*" * 30)
    result = s.calculate("1-((5-6) - (1-2))")
    assert result == 1
    print(result)

    print("*|" * 30)
    result = s.calculate("2-(1)")
    print(result)
    assert result == 1

    print("~" * 30)
    result = s.calculate("(8+4-1+8-10)")
    print(result)
    assert result == 9

    print("*|" * 30)
    result = s.calculate("2-4-(8+2-6+(8+4-(1)+8-10))")
    print(result)
    assert result == -15

    # 怎么表示表达式？
    # a + b
    # (a, b), (+)
    # a + b + c = (a + b) + c
    # ((a, b, +), c, +)
    # a + b + c + d
    # ((a, +, b), +, c), +, d)
    # new tuple: 开始的时候，和有括号的时候
    # insert into tuple, number
    # 栈不能太深，不然就爆了
