def gen_naturals():
    current=0
    while True:
        yield current
        current +=1

gen = gen_naturals()

s1 = list(range(2,80))
s2 = map(lambda x: 2*x , s1)
s3= filter(lambda x: x%2 ==0 , s1)

for _ in range(1,5):
    print(next(gen))

print("====")

print(next(gen))

print(next(gen))

def filter(iterable, fn):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter(range(5), is_even)) # a list of the values yielded from the call to filter
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    for item in iterable:
        if fn(item):
            yield item


# """
#     >>> def sequence(start, step):
#     ... while True:
#     ... yield start
#     ... start += step
#     >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
#     >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
#     >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
#     >>> [next(result) for _ in range(10)]
#     [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
#     """

def merge(a, b):
    curr,from_a,from_b =0,next(a),next(b)
    # pool_a,pool_b=[],[]
    while True:
        if from_a > from_b:
            curr = from_b
            from_b = next(b)
        elif from_a<from_b:
            curr = from_a
            from_a=next(a)
        elif from_a == from_b:
            curr= from_a
            from_a= next(a)
            from_b= next(b)
        yield curr

