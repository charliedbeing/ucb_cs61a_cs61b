def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    def f(g):
        nonlocal n
        n=g(n)
        return n
    return f

def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    """
    grouped = {}
    for item in s:
        temp = fn(item)
        if not grouped.__contains__(temp):
            grouped[temp]=[item]
        else:
            grouped[temp].append(item)
    return grouped

def add_this_many(x, el, s):
    """ Adds el to the end of s the number of times x occurs
    in s.
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 2, 2]
    """
    def help():
        nonlocal s
        i = 1;
        while i <= x:
            s.append(el)
            i = i + 1
        return s
    help()
    return s


def merge(a, b):
    """
    >>> def sequence(start, step):
    ...     while True:
    ...         yield start
    ...         start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    curr, from_a, from_b = 0, next(a), next(b)
    # pool_a,pool_b=[],[]
    while True:
        if from_a > from_b:
            curr = from_b
            from_b = next(b)
        elif from_a < from_b:
            curr = from_a
            from_a = next(a)
        elif from_a == from_b:
            curr = from_a
            from_a = next(a)
            from_b = next(b)
        yield curr