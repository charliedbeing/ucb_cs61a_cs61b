from zip.lab.lab07 import *


# """
#         >>> link = Link(1, Link(2, Link(3)))
#         >>> g = filter_link(link, lambda x: x % 2 == 0)
#         >>> next(g)
#         2
#         >>> next(g)
#         StopIteration
#         >>> list(filter_link(link, lambda x: x % 2 != 0))
#         [1, 3]
#         """

def filter_link(link,f):

    i = link
    while not i == Link.empty:
        curr, rest = i.first, i.rest
        if f(curr):
            i = rest
            yield curr

        else:
            i = rest

"""
while a return statement closes the current frame after the function exits, a yield statement causes the frame to be
saved until the next time next is called,which allows the generator to automatically keep track of the iteration state.
"""
def filter_link_2(link,f):

    if not link == Link.empty:
        curr,rest = link.first,link.rest
        if f(curr):
            filter_link_2(rest,f)
            yield curr
        else:
            filter_link_2(rest,f)

def test_filter_link_2():
    link2 = Link(108, Link(201, Link(41, Link(6))))
    g = filter_link_2(link2,lambda x: x % 2 == 0)

    ll = list(filter_link(link2, lambda x: x % 2 != 0))

    print(type(g))
    print(next(g))

    print(ll)


test_filter_link_2()



def test_filter_link():
    link = Link(1, Link(20, Link(4, Link(6))))

    link2 = Link(108, Link(20, Link(4, Link(6))))

    g = filter_link(link2, lambda x: x % 2 == 0)

    print(type(g))

    print(next(g))
    print(next(g))
    print(next(g))

    print(next(g))
    print(next(g))


def tools_add_arr(arr):
    rs =0
    for i in arr:
        rs = rs + i
    return rs

# print(tools_add_arr([10,2]))

def sum_paths_gen(t):

    def help(t,acc):
        if Tree.is_leaf(t):
            acc.append(t.label)
            yield tools_add_arr(acc)
        else:
            header,bs = t.label, t.branches
            acc.append(header)
            for branch in bs:
                temp = acc[:]
                help(branch,temp)
    yield help(t,[])

def test_sum_paths_gen():
    t1 = Tree(5)
    t2 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(9)])
    g= sum_paths_gen(t2)
    print(next(g))

    print(next(g))

# test_sum_paths_gen()




def sum_paths_gen_2(t,acc=[]):
    if Tree.is_leaf(t):
       acc.append(t.label)
       print('print>>>>>>')
       yield tools_add_arr(acc)
    else:
        header, bs = t.label, t.branches
        acc.append(header)
        for branch in bs:
            temp = acc[:]
            sum_paths_gen_2(branch, temp)


def test_spg_2():
    t2 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(9)])
    t1 = Tree(5)
    # g = sum_paths_gen_2(t1)
    #
    # print(type(g))
    # print(next(g))

    g2 = sum_paths_gen_2(t2)
    print(type(g2))




    # sum_paths_gen_2(t2)

# test_spg_2()


def sum_paths_gen_2(t):
    rec =[]

    def help(t, acc=[]):
        if Tree.is_leaf(t):
            acc.append(t.label)
            rec.append(tools_add_arr(acc))
        else:
            header, bs = t.label, t.branches
            acc.append(header)
            for branch in bs:
                temp = acc[:]
                help(branch, temp)
    help(t)
    yield from rec


def test_spg_3():
    t2 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(9)])

    g2 = sum_paths_gen_2(t2)
    print(type(g2))

    print(next(g2))
    print(next(g2))
    print(next(g2)

test_spg_3()