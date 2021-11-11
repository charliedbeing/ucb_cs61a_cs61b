from lab5_1 import *
def height(t):
    rec=[]
    def help(t,acc):
        if not is_leaf(t):
            bc=branches(t)
            acc.append(1)
            for branch in bc:
                temp=acc[:]
                help(branch,temp)
        else:
            rec.append(acc)
    help(t,[])
    return rec

def help_tool_max(arr):
    return max([len(x) for x in arr ])

def help_sum_arr(arr):
    res =0
    for item in arr:
        res = res+item
    return res

def help_tool_sum_max(arr):
    return max([help_sum_arr(x) for x in arr])

t = tree(3,[tree(5,[tree(1)]),tree(2,[tree(22,[tree(222)])])])


t2 = tree(1,[tree(2,[tree(5,[tree(55)]),tree(6)]),tree(3,[tree(7)]),tree(4,[tree(8),tree(9),tree(10)])])
# height(t)
# height(t2)
#
# print(help_tool_max(height(t2)))

def max_path_sum(t):
    rec =[]
    def help(acc,t):
        if not is_leaf(t):
            curr,bs= label(t),branches(t)
            acc.append(curr)
            for branch in bs:
                temp =acc[:]
                help(temp,branch)
        else:
            acc.append(label(t))
            rec.append(acc)

    help([],t)
    return rec

# print(help_tool_sum_max(max_path_sum(t2)))


# def square_tree(t):
#     newTree = tree(0)
#     def help(t):
#         curr,bs = label(t),branches(t)
#
#         if not is_leaf(t):
#             for branch in bs:
#                 help(branch)
#         else:
#             return tree(curr*curr)
#
#     help(t,newTree)
#
#     return newTree


def help_replace_node(t1,t2):
    pass

def square_tree_1(t):
    if not is_leaf(t):
        curr, bs = label(t), branches(t)
        newTree = tree(curr * curr, bs)
        for branch in bs:
            square_tree_1(branch)
        return newTree
    else:
        curr =label(t)
        t.append(tree(curr*curr))
tree1 = tree(3,[tree(7),tree(2)])
#
# test1 = square_tree_1(tree1)
#
# print(test1)


def suqare_tree(tree):

    def square_tree_2(tree):
        if not is_leaf(tree):
            update_tree(tree, lambda x: x * x)
            bs= branches(tree)
            for branch in bs:
                square_tree_2(branch)
        else:
            update_tree(tree, lambda x: x * x)

    square_tree_2(tree)
    print(tree)


suqare_tree(tree1)

def find_path(tree,x):
    rec = []
    def help(tree,x,acc):
        curr, brans = label(tree), branches(tree)
        acc.append(curr)
        if curr == x:
            acc.append(True)
            rec.append(acc)
        if not is_leaf(tree):
            for branch in brans:
                temp=acc[:]
                help(branch,x,temp)

    help(tree,x,[])
    print(rec)

tree2 = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])

find_path(tree2,5)

def prune_binary(t,nums):
    pass
print_tree(t)

print(t)

def copy_tree(t1):
    curr,bans =label(t1),branches(t1)
    return tree(curr,bans)

def help_is_in(s,arr):
    result = False
    for item in arr:
        if item.__contains__(s):
            result =True
            break
    return result

def help_arr_str(arr):
    result =''
    for item in arr:
        result=result+item
    return result




def help_check_branch(branches,acc,arr):
    result =[]
    for branch in branches:
        temp=acc[:]
        curr = label(branch)
        temp.append(curr)
        ok = help_is_in(help_arr_str(temp), arr)
        if ok:
            result.append(branch)
    return result


#['01','110','100']
def find_path_2(tr,arr):

    def help(t,acc):
        curr, brans, newBranches,temp_tree = label(t), branches(t),[],[]
        acc.append(curr)
        ok = help_is_in(help_arr_str(acc),arr)
        if ok:
            temp_tree = tree(curr)
            if not is_leaf(t):
                newBranches = help_check_branch(brans,acc,arr)
                temp_tree = tree(curr,newBranches)
                for branch in newBranches:
                    temp=acc[:]
                    help(branch,temp)
            return help(temp_tree,acc)
        else:
            return t

    return help(tr,[])





def find_path_3(tr,arr):

    def help(t,acc):
        curr, brans, newBranches,temp_tree = label(t), branches(t),[],[]
        acc.append(curr)
        ok = help_is_in(help_arr_str(acc),arr)
        if ok:
            temp_tree = tree(curr)
            if not is_leaf(t):
                newBranches = help_check_branch(brans,acc,arr)
                temp_tree = tree(curr,newBranches)
            return help(temp_tree,acc)
        else:
            return t

    return help(tr,[])

# test = find_path_3(t,arr)
#
# print('-------')
# print(test)
#
# print_tree(test)

def find_new_tree(tr,arr):
    """
    this is a very good example to show how to cut the branch in the three and
    """
    def help(t,acc):
        curr, brans, newBranches,temp_tree = label(t), branches(t),[],[]
        acc.append(curr)
        ok = help_is_in(help_arr_str(acc),arr)
        if ok:
            if not is_leaf(t):
                newBranches = help_check_branch(brans,acc,arr)
                update_tree_branches(t,newBranches)
                for bran in newBranches:
                    temp=acc[:]
                    help(bran,temp)

    help(tr,[])

    return tr

t = tree('1',[tree('0',[tree('0'),tree('1',[tree('1'),tree('0')])]),tree('1',[tree('0')])])
arr = ['01','110','100']
arr1 = ['1011','110']
arr1 = ['01']

print_tree(find_new_tree(t,arr1))








