# coding: utf-8

def car(s, sep):
    """
    get first split.
    :param s: string to be split
    :param sep: delimiter string
    :return: first split string
    >>> car("", ',')
    ''
    >>> car("a", ',')
    'a'
    >>> car("a,b", ',')
    'a'
    >>> car(",", ',')
    ''
    """
    result = ""

    if len(s) == 0:
        return ''

    while len(s) != 0 and s[0] != sep:
        result += s[0]
        s = s[1:]

    return result

def cdr(s, sep):
    """
    get string right after delimiter char.
    :param s: string to be split
    :param sep: delimiter string
    :return:
    >>> cdr("a", ',')
    ''
    >>> cdr("a,", ',')
    ''
    >>> cdr("a,b", ',')
    'b'
    >>> cdr("a,b,", ',')
    'b,'
    >>> cdr("a,b,c", ',')
    'b,c'
    """
    if len(s) == 0:
        return ""

    while len(s) != 0 and s[0] != sep:
        s = s[1:]

    if len(s) == 0:
        return ""
    else:
        return s[1:]

def split(s, sep):
    """
    Return a list of the words in the string, using sep as the delimiter string.
    :param s:
    :param sep:
    :return:
    >>> split("a", ',')
    ['a']
    >>> split("a,", ',')
    ['a']
    >>> split("a,,", ',')
    ['a', '']
    >>> split("a,b", ',')
    ['a', 'b']
    """
    result = []
    while len(s) != 0:
        result.append(car(s, sep))
        s = cdr(s, sep)

    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()

