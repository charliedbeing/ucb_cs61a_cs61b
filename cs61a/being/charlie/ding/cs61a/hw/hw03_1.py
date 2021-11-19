from lab5_1_1 import *

# """Returns a new tree where every leaf value equal to find_value has
#   been replaced with replace_value.
#
#   >>> yggdrasil = tree('odin',
#   ...                  [tree('balder',
#   ...                        [tree('thor'),
#   ...                         tree('freya')]),
#   ...                   tree('frigg',
#   ...                        [tree('thor')]),
#   ...                   tree('thor',
#   ...                        [tree('sif'),
#   ...                         tree('thor')]),
#   ...                   tree('thor')])
#   >>> laerad = copy_tree(yggdrasil) # copy yggdrasil for testing purposes
#   >>> print_tree(replace_leaf(yggdrasil, 'thor', 'freya'))
#   odin
#     balder
#       freya
#       freya
#     frigg
#       freya
#     thor
#       sif
#       freya
#     freya
#   >>> laerad == yggdrasil # Make sure original tree is unmodified
#   True
#   """

def replace_leaf(t, find_value, replace_value):
    another = copy_tree(t)
    def help(t1, find_value, replace_value):
        if is_leaf(t1):
            if label(t1) == find_value:
                update_tree_new_value(t1, replace_value)
        else:
            brs = branches(t1)
            for branch in brs:
                help(branch, find_value, replace_value)
        return t1;
    help(another,find_value,replace_value)
    return another



yggdrasil = tree('odin',
                  [tree('balder',
                          [tree('thor'),
                          tree('freya')]),
                    tree('frigg',
                         [tree('thor')]),
                     tree('thor',
                         [tree('sif'),
                          tree('thor')]),
                     tree('thor')])

tree1 = replace_leaf(yggdrasil,'thor','dzg')

# print_tree(tree1)


def help_for_has_path_1(arr):
    result=""
    for item in arr:
        result = result+item
    return result


def has_path(t, word):

    assert len(word) > 0, 'no path for empty word.'
    acc =[]
    rec =[]
    rec.append(False)

    def help(t,acc):
        curr,brs = label(t),branches(t)
        if curr == word and len(acc)==0:
            rec.append(True)
        if not is_leaf(t):
            temp = acc[:]
            temp.append(curr)
            for branch in brs:
                help(branch,temp)
        else:
            temp1 = acc[:]
            temp1.append(curr)
            if help_for_has_path_1(temp1) == word:
                rec.append(True)


    help(t,acc)
    if len(rec)>1:
        return True
    else:
        return False

greetings = tree('h', [tree('i'),
                          tree('e', [tree('l', [tree('l', [tree('o')])]),
                                       tree('y')])])

# print( has_path(greetings,'i'))




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

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y."""
    if upper_bound(x) >= upper_bound(y):
        return interval(lower_bound(x)-upper_bound(y), upper_bound(x)-lower_bound(y))
    else:
        return interval(lower_bound(y)-upper_bound(x),upper_bound(y)-lower_bound(x))


int1 = interval(4,7)
int2 = interval(6,15)
int1_2 = sub_interval(int1,int2)

print(int1_2)

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided by
    any value in y. Division is implemented as the multiplication of x by the
    reciprocal of y."""
    assert upper_bound(x)!= lower_bound(x) or upper_bound(y)!=lower_bound(y)
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)