from lab07.lab07 import *

def help(tree):
    if tree.is_leaf():
        return tree.label
    else:
        temp = tree.label
        for branch in tree.branches:
            temp = temp + help(branch)
        return temp

t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])

t= Tree(3, [Tree(5)])
test_sum = help(t)


def cumulative_sum(t):

    if t.is_leaf():
        return Tree(help(t))
    else:
        head, bs = t.label, t.branches
        for branch in bs:

        cumulative_sum(Tree(help(t), bs))


test_2 = cumulative_sum(t)

print(test_2)
