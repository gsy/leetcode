from all_oone_data_structure import AllOne

if __name__ == '__main__':
    obj = AllOne()
    obj.inc("foo")
    # obj.dec(key)
    max_key = obj.getMaxKey()
    min_key = obj.getMinKey()
    print(max_key)
    print(min_key)

    print('-' * 30)
    obj = AllOne()
    obj.inc("foo")
    obj.inc("bar")
    obj.inc("foo")
    # obj.dec(key)
    max_key = obj.getMaxKey()
    min_key = obj.getMinKey()
    print(max_key)
    assert max_key == "foo"
    print(min_key)
    assert min_key == "bar"

    print('-' * 30)
    obj = AllOne()
    obj.inc("foo")
    obj.inc("bar")
    obj.inc("foo")
    obj.dec("foo")
    max_key = obj.getMaxKey()
    min_key = obj.getMinKey()
    print("max", max_key)
    print("min", min_key)

    print('-' * 30)
    obj = AllOne()
    obj.inc("foo")
    obj.inc("bar")
    obj.inc("foo")
    obj.dec("foo")
    obj.dec("foo")
    max_key = obj.getMaxKey()
    min_key = obj.getMinKey()
    print("max", max_key)
    print("min", min_key)

    print('-' * 30)
    obj = AllOne()
    obj.inc("foo")
    obj.inc("bar")
    obj.inc("foo")
    obj.dec("foo")
    obj.dec("foo")
    obj.dec("boom")
    obj.inc("boom")
    obj.dec("boom")
    max_key = obj.getMaxKey()
    min_key = obj.getMinKey()
    print("max", max_key)
    print("min", min_key)

    print('-' * 30)
    obj = AllOne()
    obj.inc("a")
    obj.inc("b")
    obj.inc("b")
    obj.inc("b")
    obj.inc("b")
    obj.dec("b")
    obj.dec("b")
    max_key = obj.getMaxKey()
    min_key = obj.getMinKey()
    print("max", max_key)
    print("min", min_key)

    print('-' * 30)
    obj = AllOne()
    obj.inc("hello")
    obj.inc("goodbye")
    obj.inc("hello")
    obj.inc("hello")
    max_key = obj.getMaxKey()
    print("max", max_key)
    obj.inc("leet")
    obj.inc("code")
    obj.inc("leet")
    obj.dec("hello")

    obj.inc("leet")
    obj.inc("code")
    obj.inc("code")

    max_key = obj.getMaxKey()
    print("max", max_key)

    obj = AllOne()
    obj.inc("hello")
    obj.inc("hello")
    max_key = obj.getMaxKey()
    min_key = obj.getMinKey()
    print(max_key)
    assert max_key == "hello"
    print(min_key)
    assert min_key == "hello"
    obj.inc("leet")
    max_key = obj.getMaxKey()
    min_key = obj.getMinKey()
    print(max_key)
    assert max_key == "hello"
    print(min_key)
    assert min_key == "leet"