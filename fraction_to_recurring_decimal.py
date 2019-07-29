# -*- coding: utf-8 -*-


class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if denominator == 0:
            return None
        elif numerator == 0:
            return "0"

        minus = False
        if (numerator < 0 and denominator) > 0 or (numerator > 0 and denominator < 0):
            minus = True

        numerator = abs(numerator)
        denominator = abs(denominator)

        result, recurve, dot = "", {}, None
        while numerator > 0:
            if numerator < denominator:
                numerator = numerator * 10
                if dot is None:
                    dot = len(result)

            if numerator in recurve:
                start = recurve[numerator]
                if dot <= start:
                    result = result[:start] + "({})".format(result[start:])
                else:
                    result = result + "({})".format(result[start:])
                break

            current = int(numerator / denominator)
            result = result + str(current)
            recurve[numerator] = len(result) - 1
            numerator = numerator % denominator

        if dot is not None:
            if dot == 0:
                result = "0." + result
            elif dot > 0:
                result = result[:dot] + "." + result[dot:]
        if minus:
            result = "-" + result
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.fractionToDecimal(1, 2)
    print(r)
    assert r == "0.5"

    r = s.fractionToDecimal(2, 1)
    assert r == "2"

    r = s.fractionToDecimal(10, 2)
    assert r == "5"

    r = s.fractionToDecimal(2, 10)
    assert r == "0.2"

    r = s.fractionToDecimal(3, 7)
    print(r)
    assert r == "0.(428571)"

    r = s.fractionToDecimal(30, 7)
    print(r)
    assert r == "4.28571(428571)"

    r = s.fractionToDecimal(1, 3)
    print(r)
    assert r == "0.(3)"

    r = s.fractionToDecimal(10, 3)
    print(r)
    assert r == "3.(3)"

    r = s.fractionToDecimal(50, 8)
    print(r)
    assert r == "6.25"

    r = s.fractionToDecimal(-50, 8)
    print(r)
    assert r == "-6.25"

    r = s.fractionToDecimal(-22, 2)
    print(r)
    assert r == "-11"

    r = s.fractionToDecimal(-22, -2)
    print(r)
    assert r == "11"
