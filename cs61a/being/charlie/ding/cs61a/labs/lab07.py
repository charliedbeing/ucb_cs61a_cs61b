
from zip.lab07.lab07 import *

class Naturals:
    def __init__(self):
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        return self.current

def test_naturals():
    m = Naturals()

    print(type(m))
    print(next(m))
    print(next(m))
    print(next(m))
    print(m.current)

def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>
    >>> list(s)
    [5, 25, 10]

    >>> m = scale(Naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    for item in s:
        yield item * k


def link_to_list(link):
    """Takes a linked list and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> link_to_list(Link.empty)
    []
    """
    rec =[]

    def help(link):
        if not link == Link.empty:
            head, rest = link.first, link.rest
            if not rest == Link.empty:
                rec.append(head)
                help(rest)
            else:
                rec.append(head)

    def help_2(link):
        while not link == Link.empty:
            head,rest = link.first,link.rest
            rec.append(head)
            link = rest



    # help(link)
    help_2(link)
    return rec
# """Mutates t so that each node's label becomes the sum of all labels in
#     the corresponding subtree rooted at t.
#
#     >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
#     >>> cumulative_sum(t)
#     >>> t
#     Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
#     """


def cumulative_sum(t):

    def help(tree):
        if tree.is_leaf():
            return tree.label
        else:
            temp = tree.label
            for branch in tree.branches:
                temp = temp + help(branch)
            return temp

    if t.is_leaf():
        return Tree(help(t))
    else:
        head,bs = t.label, t.branches
        temp = Tree(help(t))
        for branch in bs:
            temp.branches.append(help(branch))
        return temp


