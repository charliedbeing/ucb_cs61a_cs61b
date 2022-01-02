from lib import *

# a = Link(1,Link(2,Link(3,Link(4,Link(5)))))
#
# print(len(a))
#
# print(a[3])
#
# b = str('ava')
#
# print(len(b))
#
# print(b[2])

def is_palindrome(seq):
    def help(s,flag):
        rs,i,j='',0,len(s)-1
        if 'left' == flag:
            while i<= len(s)-1:
                rs = rs + s[i]
                i = i+1
        elif 'right' == flag:
            while j>= 0:
                rs = rs +s[j]
                j = j-1
        return rs
    left,right = help(seq,'left'), help(seq,'right')
    return left == right

print(is_palindrome('ava'))

print(is_palindrome(Link('a',Link('v',Link('a')))))


def sum_nums(lnk):

    def help(lnk,acc):
        if lnk == Link.empty:
            return acc
        else:
            return help(lnk.rest,acc+lnk.first)
    return help(lnk,0)

# a = Link(1,Link(6,Link(7)))
#
# print(sum_nums(a))

def multipy(acc):
    rs,i,count =1,0,len(acc)
    while i <= count-1:
        rs = rs* acc[i]
        i =i+1
    return rs


def multiply_lnks(lst_of_lnks):
    count = min([len(x) for x in lst_of_lnks])

    def help(n):
        i,temp = 1, multipy([x[0] for x in lst_of_lnks])
        rs = Link(temp)
        curr = rs
        while i <= n - 1:
            temp = multipy([x[i] for x in lst_of_lnks])
            curr.rest = Link(temp)
            i = i+1
            curr = curr.rest
        return rs

    return help(count)

a = Link(2, Link(3, Link(5)))
b = Link(6, Link(4, Link(2)))
c = Link(4, Link(1, Link(0, Link(2))))
p = multiply_lnks([a, b, c])

print(p)

print(p.rest.first)

print(p.rest.rest.rest is Link.empty)
