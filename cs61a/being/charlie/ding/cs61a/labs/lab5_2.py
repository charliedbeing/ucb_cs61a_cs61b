from lab5_1 import *

t1  = tree("nihao")

# print(label(t1))
#
# print(len(branches(t1)))


def have_one_true(arr):
    rec=False
    for item in arr:
        if item:
            rec=True
    return rec

def berry_finder(t):
    rec =[]
    def help(t):
        curr,left=label(t),branches(t)
        if curr == 'berry':
            rec.append(True)
            return rec
        else:
            rec.append(False)
            for b in left:
                help(b)
    help(t)
    return have_one_true(rec)


sproul = tree('roots', [tree('branch1', [tree('charlie'), tree('berry')]), tree('branch2')])

# print(berry_finder(sproul))


def help_leaves_nodes(arr):
    rec=[]
    for i in arr:
        rec.append(tree(i))
    return rec

def sprout_leaves(t, leaves):
    bs = help_leaves_nodes(leaves)

    def help(t):
        curr,left = label(t),branches(t)
        if is_leaf(t):
            temp = bs
            t.extend(temp)
        else:
            brans= branches(t)
            for bran in brans:
                help(bran)
    help(t)
    return t

# t1 = tree(1, [tree(2), tree(3)])
#
# print(t1)
# new1 = sprout_leaves(t1,[4,5])
#
# print(new1)
#
# print_tree(new1)

# """
#     >>> seq = [-4, -2, 0, 1, 3]
#     >>> fn = lambda x: x**2
#     >>> coords(fn, seq, 1, 9)
#     [[-2, 4], [1, 1], [3, 9]]
#     """

def coords(fn, seq, lower, upper):
    """ wow, this is the power of nest or """
    return [[seq[x],fn(seq[x])] for x in [seq.index(x) for x in [ x for x in seq if (fn(x)>= lower and fn(x)<= upper)]]]

seq = [-4, -2, 0, 1, 3]
fn = lambda x: x**2
test = coords(fn, seq, 1, 9)

# print(test)

def riffle(desk):
    return [[desk[x],desk[(len(desk)//2)+x]] for x in [ desk.index(x) for x in desk] if x<= len(desk)/2-1]

test2 = riffle(range(20))

# print(test2)

t1= tree(2)
t2 =tree(3,[tree(4),tree(5),tree(6)])
t3 =tree(3,[tree(4),tree(5),tree(6,[tree(61),tree(62)])])

t4 =tree(3,[tree(4,[tree(41),tree(42)]),tree(5),tree(6,[tree(61),tree(62)])])

# print(t1)
# print(t2)
# print(t3)

def zip_tree(t1,t2):
    pass

def iter_tree(t):
    curr,bs = label(t),branches(t)
    print(curr)
    for b in bs:
        iter_tree(b)

def iter_tree_2(t):
    def help(t,acc):
        curr, bs = acc + str(label(t)), branches(t)
        print(curr)
        acc= acc+'-'
        for b in bs:
            help(b,acc)
    help(t,'-')

print('=========')
print(t3)
print(t4)

iter_tree_2(t3)
print('-----')
iter_tree_2(t4)
#
#



def arr_op(arr1,arr2):
    """
    [3, [4], [5], [6, [61], [62]]]
    [3, [4, [41], [42]], [5], [6, [61], [62]]]
    """
    l1,l2,rec,i= len(arr1),len(arr2),[],0
    count =max(l1,l2)
    while i<= count-1:
        if i==0:
            temp = arr1[i]+arr2[i]
            rec.append(temp)
        elif i<=l1-1 and i<=l2-1 :
            rec.append(arr_op(arr1[i],arr2[i]))
        elif i>l1-1:
            rec.extend(arr2[i:])
            break
        elif i>l2-1:
            rec.extend(arr1[i:])
            break
        i=i+1

    return rec

ta1=  [3, [4], [5], [6, [61], [62]]]
ta2 =  [3, [4, [41], [42]], [5], [6, [61], [62]]]



# test = arr_op(ta1,ta2)
#
# print(test)
#
#
# print_tree(arr_op(tree(2), tree(3, [tree(4), tree(5)])))
#
#
# print_tree(arr_op(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))



taa1 =tree(2, [tree(3)])
taa2 = tree(2, [tree(3), tree(4)])

print(taa1)
print(taa2)

print(arr_op([2, [3]],[2, [3], [4]]))

