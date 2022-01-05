from zip.lab08.lab08 import *

def help(link):
    rs = Link(link.first)
    p = rs
    def help_(link):
        nonlocal rs
        while not link == Link.empty:
            rs.rest = Link(link.first)
            rs =rs.rest
            link = link.rest
    help_(link.rest)
    return p

def test_help():
    lst1 = Link(1,Link(2,Link(3)))
    lst2 = help(lst1)


    print(lst1)

    print(lst2)

    lst2.first =100

    print(lst1)
    print(lst2)

# test_help()



def insert(link,value,index):
    pre,curr,i,copy = link,link,0,help(link)
    while not link == Link.empty:
        if i == index:
            if pre != curr:
                new_node = Link(value)
                pre.rest = new_node
                new_node.rest = curr
                break
            else:
                new_node =Link(value,pre)
                link.first = value
                link.rest = copy

                break
        else:
            i = i+1
            pre = link
            link = link.rest
            curr = link


    if index >i:
        raise IndexError


def test_insert():
    link = Link(1,Link(2,Link(3)))
    print(link)
    insert(link,9001,0)
    print(link)
    insert(link, 100, 27)
    print(link)

# # test_insert()
# def help_tool_1(arr,rest):
#     rec=[]
#     for i in rest:
#         temp =arr[:]
#         rec.append(temp.append(i))
#     return rec
#
# def help(arr,n,acc=[]):
#     if n == 1 and len(acc) ==0:
#         if len(arr) == 1:
#             acc.append([arr[0]])
#             return acc
#         else:
#             curr,rest = arr[0],arr[1:]
#             acc.append([curr])
#             return help(rest,n,acc)
#     elif n==1 and len(acc)>0:
#         for item in acc:
#             if  len(item)< 2:
#                item = help_tool_1(item,arr)
#         return
#
#     elif n>1:
#         curr,rest = arr[0],arr[1:]
#         if len(acc)>1:
#             pass
#         else:
#             acc.append([curr])
#             return help(rest,n-1,acc)
#
#
#
#
# def test_help():
#     arr=[1,2,3]
#     t = help(arr,1)
#     print(t)
#
# test_help()
#
# def find_value_from_set(arr,n):
#     rec=[]
#     def help(arr,n):
#         if n==1:
#             if len(arr)==1:
#                 return arr[0]
#             else:
#                 return [arr[0],help(arr[1:],n)]
#
#
#
#
#
# def insert_into_all(item,nested_list):
#     pass

"""
[1,2,3,4,5,6] arr  get 4 items n
f(arr,n) = g(arr[0],arr[1:])+ g(arr[1],arr[2:])+g(arr[2],arr[3:])
g(curr=[],arr=[])

"""
def subseqs(s):
    rec =[]
    def help(pre=[],curr=[],arr=[],target=1):
        if len(curr) == target:
            rec.append(curr)
            if len(arr)>0:
                help(pre,pre,arr,target)
        elif len(curr)< target:
            pre=curr[:]
            if len(arr)>0:
                curr.append(arr[0])
                help(pre, curr, arr[1:], target)


    # def help_(pre=[], curr=[], arr=[], target=1):
    #     if len(curr) == target:
    #         rec.append(curr)
    #         if len(arr) > 0:
    #             help(pre, pre, arr, target)
    #     elif len(curr) < target:
    #         pre = curr[:]
    #         curr.append(arr[0])
    #         help(pre, curr, arr[1:], target)


    # def to_last_step(curr=[],arr=[],target=1):
    #     if len(curr)+1 == target:
    #         help(curr,curr,arr,target)
    #     elif len(curr)+len(arr) == target:
    #         rec.append(curr.extend(arr))
    #     while len(curr)+ len(arr) > target:
    #         pre = curr[:]
    #         curr.append(arr[0])
    #         arr = arr[1:]
    #         to_last_step(pre,arr,target)
    #         to_last_step(curr, arr, target)

    # def to_last_step_2(pre,curr=[],arr=[],target =1):
    #     if len(curr) == target:
    #         rec.append(curr)
    #         return
    #     if len(curr)+1 == target:
    #         help(curr,curr,arr,target)
    #         return
    #     elif len(curr) < target -1:
    #         curr.append(arr[0])
    #         to_last_step_2(pre,curr,arr[1:],target)
    #     elif len(curr) + len(arr) == target:
    #         curr.extend(arr)
    #         rec.append(curr)
    #     for i,v in enumerate(arr[1:]):
    #         curr=pre[:]
    #         if len(curr)+len(arr)-1-i+1 >= target:
    #             temp =pre[:]
    #             temp.append(v)
    #             to_last_step_2(pre,temp,arr[i+2:],target)

    def to_last_step_3(pre,curr=[],arr=[],target =1):
        if len(curr) == target:
            rec.append(curr)
            return
        if len(curr)+1 == target:
            help(curr,curr,arr,target)
            return
        elif len(curr) < target -1:
            curr.append(arr[0])
            rest = arr[1:]
            if len(curr)<target -1:
                for i, v in enumerate(rest):
                    if len(curr) + len(arr) - 1 - i + 1 >= target:
                        temp = curr[:]
                        temp.append(v)
                        to_last_step_3(pre, temp, rest[i + 1:], target)
            else:
                to_last_step_3(pre, curr, arr[1:], target)

        elif len(curr) + len(arr) == target:
            curr.extend(arr)
            rec.append(curr)
        for i,v in enumerate(arr[1:]):
            curr=pre[:]
            if len(curr)+len(arr)-1-i+1 >= target:
                temp =pre[:]
                temp.append(v)
                to_last_step_3(pre,temp,arr[i+2:],target)


    def out_help(s,i):
        j,count = 0,len(s)-1-(i-1)
        while j<=count:
            to_last_step_3([s[j]],[s[j]],s[j+1:],i)
            j =j +1


    i,count = 1, len(s)
    while i <= count:
        if i ==5:
            out_help(s,i)
        i=i+1

    return rec

def test_subseqs():
    s =[1,2,3,4,5,6]
    t = subseqs(s)
    print(t)

test_subseqs()























