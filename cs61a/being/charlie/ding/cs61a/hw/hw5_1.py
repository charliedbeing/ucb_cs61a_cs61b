from lib import *

t1 = Tree(1, [Tree(2, [Tree(3), Tree(4, [Tree(6)]), Tree(5)]), Tree(5)])


# print(t1)
#
# print(type(t1))

def tool_array(arr):
    rs = ''
    for i in arr:
        rs = rs + str(i)
    return rs


def paths(t, node):
    rec = []

    def help(tt, nd, acc):
        curr, rest = tt.label, tt.branches
        acc.append(curr)
        if curr == nd:
            rec.append(acc)
            print(tool_array(acc))
        for branch in rest:
            temp = acc[:]
            help(branch, nd, temp)

    help(t, node, [])
    return rec


test1 = paths(t1, 5)

print(test1)


# """Remove all the nodes containing value in link. Assume that the
#     first element is never removed.
#
#     >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
#     >>> print(l1)
#     <0 2 2 3 1 2 3>
#     >>> remove_all(l1, 2)
#     >>> print(l1)
#     <0 3 1 3>
#     >>> remove_all(l1, 3)
#     >>> print(l1)
#     <0 1>
#     >>> remove_all(l1, 3)
#     >>> print(l1)
#     <0 1>
#     """

def remove_all(link, value):
    rs = Link(link.first)
    curr_p = rs

    def help(link, item):
        nonlocal curr_p
        curr, rest = link.first, link.rest
        if rest == Link.empty:
            if not curr == item:
                curr_p.rest = Link(curr)
        else:
            if curr == item:
                help(rest, item)
            else:
                curr_p.rest = Link(curr)
                curr_p = curr_p.rest
                help(rest, item)

    help(link.rest, value)
    return rs


l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))


test_r = remove_all(l1,2)

print(test_r)

# """Return a Link with the same structure as link but with fn mapped over
#     its elements. If an element is an instance of a linked list, recursively
#     apply f inside that linked list as well.
#
#     >>> s = Link(1, Link(Link(2, Link(3)), Link(4)))
#     >>> print(deep_map(lambda x: x * x, s))
#     <1 <4 9> 16>
#     >>> print(s) # unchanged
#     <1 <2 3> 4>
#     >>> print(deep_map(lambda x: 2 * x, Link(s, Link(Link(Link(5))))))
#     <<2 <4 6> 8> <<10>>>
#     """

def deep_map(f, link):
    head,rest = link.first,link.rest
    rs = Link(f(head))
    curr_p = rs

    def help(f,link):
        nonlocal curr_p
        curr,rest = link.first,link.rest
        if rest == Link.empty:
            curr_p.rest = Link(f(curr))
        else:
            curr_p.rest = Link(f(curr))
            curr_p = curr_p.rest
            help(f,rest)
    help(f,rest)
    return rs

# s = Link(1, Link(Link(2, Link(3)), Link(4)))

s = Link(1, Link(3,Link(4)))
# print(deep_map(lambda x: x * x, s))


def deep_map_2(f, link):
    head,rest = link.first,link.rest
    if not isinstance(head,Link):
        rs = Link(f(head))
        curr_p = rs
    else:
        rs = deep_map(f,head)
        curr_p = rs

    def help(f,link):
        nonlocal curr_p
        curr,rest = link.first,link.rest
        if not isinstance(curr,Link):
            if rest == Link.empty:
                curr_p.rest = Link(f(curr))
            else:
                curr_p.rest = Link(f(curr))
                curr_p = curr_p.rest
                help(f, rest)
        else:
            help(f,curr)

    help(f,rest)
    return rs

ss = Link(1, Link(Link(2, Link(3)), Link(4)))

# print(deep_map_2(lambda x: x * x, ss))

def deep_map_3(f, link):
    if not link == Link.empty:
        curr, rest = link.first, link.rest
        if not isinstance(curr, Link):
            link.update(f(curr))
        else:
            deep_map_3(f, curr)
        deep_map_3(f, rest)


# deep_map_3(lambda x: x * x, ss)
#
# print(ss)
print('=======')

# s = Link(1, Link(Link(2, Link(3)), Link(4)))

def deep_map_4(f,link):

    def help(f,link):
        if not link == Link.empty:
            curr, rest = link.first, link.rest
            if not isinstance(curr, Link):
                return Link(f(curr),help(f,rest))
            else:
                return Link(help(f,curr),help(f,rest))
        else:
            return Link.empty

    return help(f,link)

test4 = deep_map_4(lambda x: x * x, ss)

print(test4)








