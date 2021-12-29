from zip.lab07.lab07 import *


def help(tree):
    if tree.is_leaf():
        return tree.label
    else:
        temp = tree.label
        for branch in tree.branches:
            temp = temp + help(branch)
        return temp

t = Tree(1, [Tree(3, [Tree(5,[Tree(2)])]), Tree(7)])

# t= Tree(3, [Tree(5)])
test_sum = help(t)


def cumulative_sum(t):

    if t.is_leaf():
        t.update(help(t))
    else:
        bs = t.branches
        t.update(help(t))
        for branch in bs:
           cumulative_sum(branch)

# cumulative_sum(t)
#
# print(t)

def cumulative_sum_2(t):

    if t.is_leaf():
        return Tree(help(t))
    else:
        bs = t.branches
        return Tree(help(t),[cumulative_sum_2(x) for x in bs])

test_2 = cumulative_sum_2(t)

print(test_2)


def help_max_in_left(t,f):
    if Tree.is_leaf(t):
        return t.label
    else:
        return f(t.label, f([help_max_in_left(x,f) for x in t.branches]))

t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])


t2 = Tree(2, [Tree(1), Tree(4)])
t3 = Tree(7, [Tree(7), Tree(8)])
# print(">>>>")
# print(help_max_in_left(t2,max))
# print("<<<<<")
# print(help_max_in_left(t3,min))

def is_bst_(t):
    is_or_not =True

    def help_size(t):
        if Tree.is_leaf(t):
            return True
        else:
            branches = t.branches
            return len(branches) <= 2

    def help_max_in_left(t, f):
        if Tree.is_leaf(t):
            return t.label
        else:
            return f(t.label, f([help_max_in_left(x, f) for x in t.branches]))

    def help_great_left(t):
        curr,rest = t.label, t.branches
        if len(rest) >1:
            return curr >= help_max_in_left(rest[0], max)
        else:
            return True

    def help_less_right(t):
        curr,rest = t.label, t.branches
        if len(rest) > 1:
            return curr < help_max_in_left(rest[1], min)
        else:
            return True


    def iterator_all(t):
        nonlocal is_or_not
        if not Tree.is_leaf(t):
            size,left,right = help_size(t), help_great_left(t),help_less_right(t)
            if not (size and left and right):
                is_or_not = False
                return
            rest = t.branches
            for branch in rest:
                iterator_all(branch)

    iterator_all(t)

    return is_or_not

print("======")
t2 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
print(is_bst_(t2))



def is_bst(t):
    """Returns True if the Tree t has the structure of a valid BST.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    >>> t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
    >>> is_bst(t7)
    False
    """
    is_or_not = True

    def help_size(t):
        if Tree.is_leaf(t):
            return True
        else:
            branches = t.branches
            return len(branches) <= 2

    def help_max_in_left(t, f):
        if Tree.is_leaf(t):
            return t.label
        else:
            return f(t.label, f([help_max_in_left(x, f) for x in t.branches]))

    def help_great_left(t):
        curr, rest = t.label, t.branches
        if len(rest) > 1:
            return curr >= help_max_in_left(rest[0], max)
        else:
            return True

    def help_less_right(t):
        curr, rest = t.label, t.branches
        if len(rest) > 1:
            return curr < help_max_in_left(rest[1], min)
        else:
            return True

    def iterator_all(t):
        nonlocal is_or_not
        if not Tree.is_leaf(t):
            if not (help_size(t) and help_great_left(t) and help_less_right(t)):
                is_or_not = False
            rest = t.branches
            for branch in rest:
                iterator_all(branch)

    iterator_all(t)

    return is_or_not
