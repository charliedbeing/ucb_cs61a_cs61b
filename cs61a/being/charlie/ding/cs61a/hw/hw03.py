from lab5_1_1 import *

def mobile(left, right):
    """Construct a mobile from a left arm and a right arm."""
    assert is_arm(left), "left must be a arm"
    assert is_arm(right), "right must be a arm"
    return ['mobile', left, right]

def is_mobile(m):
    """Return whether m is a mobile."""
    return type(m) == list and len(m) == 3 and m[0] == 'mobile'

def left(m):
    """Select the left arm of a mobile."""
    assert is_mobile(m), "must call left on a mobile"
    return m[1]

def right(m):
    """Select the right arm of a mobile."""
    assert is_mobile(m), "must call right on a mobile"
    return m[2]

def arm(length, mobile_or_planet):
    """Construct a arm: a length of rod with a mobile or planet at the end."""
    assert is_mobile(mobile_or_planet) or is_planet(mobile_or_planet)
    return ['arm', length, mobile_or_planet]

def is_arm(s):
    """Return whether s is a arm."""
    return type(s) == list and len(s) == 3 and s[0] == 'arm'

def length(s):
    """Select the length of a arm."""
    assert is_arm(s), "must call length on a arm"
    return s[1]

def end(s):
    """Select the mobile or planet hanging at the end of a arm."""
    assert is_arm(s), "must call end on a arm"
    return s[2]

def planet(size):
    """Construct a planet of some size."""
    assert size > 0
    return ['planet',size]

def size(w):
    """Select the size of a planet."""
    assert is_planet(w), 'must call size on a planet'
    return w[1]

def is_planet(w):
    """Whether w is a planet."""
    return type(w) == list and len(w) == 2 and w[0] == 'planet'


def examples():
    t = mobile(arm(1, planet(2)),
               arm(2, planet(1)))
    u = mobile(arm(5, planet(1)),
               arm(1, mobile(arm(2, planet(3)),
                              arm(3, planet(2)))))
    v = mobile(arm(4, t), arm(2, u))
    return (t, u, v)

def total_weight(m):
    """Return the total weight of m, a planet or mobile.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    """
    if is_planet(m):
        return size(m)
    else:
        assert is_mobile(m), "must get total weight of a mobile or a planet"
        return total_weight(end(left(m))) + total_weight(end(right(m)))

def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(arm(3, t), arm(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(arm(1, v), arm(1, w)))
    False
    >>> balanced(mobile(arm(1, w), arm(1, v)))
    False
    """
    left_arm,right_arm = left(m),right(m)
    left_torque= length(left_arm)* total_weight(end(left_arm))
    right_torque= length(right_arm) * total_weight(end(right_arm))

    if left_torque == right_torque:
        if is_mobile(end(left_arm)) and is_mobile(end(right_arm)):
            return balanced(end(left_arm)) and balanced(end(right_arm))
        elif is_mobile(end(left_arm)) and  is_planet(end(right_arm)):
            return balanced(end(left_arm))
        elif is_planet(end(left_arm)) and  is_mobile(end(right_arm)):
            return  balanced(end(right_arm))
        elif is_planet(end(left_arm)) and is_planet(end(right_arm)):
            return True
    else:
        return False

def totals_tree(m):
    """Return a tree representing the mobile with its total weight at the root.
    >>> t, u, v = examples()
    >>> print_tree(totals_tree(t))
    3
      2
      1
    >>> print_tree(totals_tree(u))
    6
      1
      5
        3
        2
    >>> print_tree(totals_tree(v))
    9
      3
        2
        1
      6
        1
        5
          3
          2
    """
    sum_weight = total_weight(m)
    left_part,right_part = end(left(m)),end(right(m))
    if is_planet(left_part) and is_planet(right_part):
        return tree(sum_weight,[tree(size(left_part)),tree(size(right_part))])
    elif is_mobile(left_part) and is_mobile((right_part)):
        return tree(sum_weight,[totals_tree(left_part),totals_tree(right_part)])
    elif is_mobile(left_part) and is_planet(right_part):
        return tree(sum_weight,[totals_tree(left_part),tree(size(right_part))])
    elif is_planet(left_part) and is_mobile(right_part):
        return tree(sum_weight,[tree(size(left_part)),totals_tree(right_part)])


def replace_leaf(t, find_value, replace_value):
    """Returns a new tree where every leaf value equal to find_value has
    been replaced with replace_value.

    >>> yggdrasil = tree('odin',
    ...                  [tree('balder',
    ...                        [tree('thor'),
    ...                         tree('freya')]),
    ...                   tree('frigg',
    ...                        [tree('thor')]),
    ...                   tree('thor',
    ...                        [tree('sif'),
    ...                         tree('thor')]),
    ...                   tree('thor')])
    >>> laerad = copy_tree(yggdrasil) # copy yggdrasil for testing purposes
    >>> print_tree(replace_leaf(yggdrasil, 'thor', 'freya'))
    odin
      balder
        freya
        freya
      frigg
        freya
      thor
        sif
        freya
      freya
    >>> laerad == yggdrasil # Make sure original tree is unmodified
    True
    """
    another = copy_tree(t)
    def help(t, find_value, replace_value):
        if is_leaf(t):
            if label(t) == find_value:
                update_tree_new_value(t, replace_value)
        else:
            brs = branches(t)
            for branch in brs:
                help(branch, find_value, replace_value)
        return t

    help(another, find_value, replace_value)
    return another

def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(tree(2, [tree(4, [tree(6)])]))
    [2, 4, 6]
    """
    acc=[]
    def help(t):
        curr,brs = label(t),branches(t)
        acc.append(curr)
        if not is_leaf(t):
            for branch in brs:
                help(branch)
    help(t)
    print(acc)

def help_for_has_path_1(arr):
    result=""
    for item in arr:
        result = result+item
    return result

def has_path(t, word):
    """Return whether there is a path in a tree where the entries along the path
    spell out a particular word.

    >>> greetings = tree('h', [tree('i'),
    ...                        tree('e', [tree('l', [tree('l', [tree('o')])]),
    ...                                   tree('y')])])
    >>> print_tree(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path(greetings, 'h')
    True
    >>> has_path(greetings, 'i')
    False
    >>> has_path(greetings, 'hi')
    True
    >>> has_path(greetings, 'hello')
    True
    >>> has_path(greetings, 'hey')
    True
    >>> has_path(greetings, 'bye')
    False
    """
    assert len(word) > 0, 'no path for empty word.'
    acc = []
    rec = []
    rec.append(False)

    def help(t, acc):
        curr, brs = label(t), branches(t)
        if curr == word and len(acc)==0:
            rec.append(True)
        if not is_leaf(t):
            temp = acc[:]
            temp.append(curr)
            for branch in brs:
                help(branch, temp)
        else:
            temp1 = acc[:]
            temp1.append(curr)
            if help_for_has_path_1(temp1) == word:
                rec.append(True)

    help(t, acc)
    if len(rec) > 1:
        return True
    else:
        return False

def interval(a, b):
    """Construct an interval from a to b."""
    return [a, b]

def lower_bound(x):
    """Return the lower bound of interval x."""
    return min(x[0],x[1])

def upper_bound(x):
    """Return the upper bound of interval x."""
    return max(x[0],x[1])

def mul_interval(x,y):
    return interval(lower_bound(x)*lower_bound(y),upper_bound(x)*upper_bound(y))

inter1 = interval(4,7)

inter2 =interval(10,100)

inter3= mul_interval(inter1,inter2)

print(inter3)



