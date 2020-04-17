def fibonacci(m):
    n, a, b= 0, 0, 1
    while n < m:
        yield a
        a, b= b, a+b
        n = n + 1

def myextend(alist):
    result = []
    for item in alist:
        print item, isinstance(item, list)
        if isinstance(item, list):
            result.extend(myextend(item))
        else:
            result.append(item)

    return result

def test(x,l=[]):
    for o in range(x):
        l.append(o)
    print l


def unique(ls):
    result = []
    [result.append(x) for x in ls if x not in result]
    return result




if __name__ == "__main__":
    for x in fibonacci(10):
        print x

    print myextend([4,5, [6]])
    result = myextend([1, 2, 3, [4, 5, [6]]])
    print "extend:", result

    test(3)                     # [0, 1, 2]
    test(1,[3,2,1])             # [3, 2, 1, 0]
    test(3)                     # [0, 1, 2, 0, 1, 2]

    print "unique:", unique([1, 2, 3, 2, 2, 4])
