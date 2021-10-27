# acc=[1,5,10,25] n =100   all possible composes  sum (number in acc ) = 100

from getSet import *


def help_parts(acc,n):
    index =0
    while acc[index]<= n and (index <len(acc)-1):
        index = index +1
    return index+1



def help_set_left_sum(acc):
    # acc=[1,5,10,25] return 1+5+10
    total,index,i = 0,len(acc)-1,0
    while i< index:
        total = total +acc[i]
        i= i+1
    return total

def help_set_sum(acc):
    # acc=[1,5,10,25] return 1+5+10+25
    total,index,i = 0,len(acc)-1,0
    while i<= index:
        total = total +acc[i]
        i= i+1
    return total

def help_set_max(acc):
    # acc=[1,5,10,25] return 25
    index = len(acc)-1
    return acc[index]

def help_set_remove_max(acc):
    # acc=[1,5,10,25] return [1,5,10]; acc=[1,5,10] return [1,5]
    count = len(acc)-1
    rec, i = [0] * count, 0
    while (i <= count - 1):
        rec[i] = acc[i]
        i= i+1
    return rec




def help_maxTimes(total,setNumbers):
    sizeOfSet,next,curr,setTotal= len(setNumbers),True,0,help_set_sum(setNumbers)
    if sizeOfSet ==1:
        next =( total % help_set_max(setNumbers)) != 0
        if (not next):
            curr=1
    elif (sizeOfSet>1 and setTotal <= total):
        curr= (total - help_set_left_sum(setNumbers))//help_set_max(setNumbers)
    elif(setTotal>total):
        next=False
    return (next,curr)






# return the count of solutions. partition
# resolve this situation  f([1,5,10],25)
# def help_old(setNumbers,total):
#     next, maxTimes = help_maxTimes(total, setNumbers)
#     if (not next):
#         return maxTimes
#     else:
#         temp, index = 0, 1
#         curr, left = help_set_max(setNumbers), help_set_remove_max(setNumbers)
#         while index <= maxTimes:
#             temp = temp + help(left, total - curr * index)
#             index = index + 1
#         return temp

def help_count(acc,total):
    def help(setNumbers, total):
        next, maxTimes = help_maxTimes(total, setNumbers)
        if (not next):
            return maxTimes
        else:
            temp, index = 0, 1
            curr, left = help_set_max(setNumbers), help_set_remove_max(setNumbers)
            while index <= maxTimes:
                temp = temp + help(left, total - curr * index)
                index = index + 1
            return temp
    resultValue,i,count =0,0,len(acc)
    while i<=count-1:
        resultValue = resultValue+ help(acc[i],total)
        i =i+1
    return resultValue




def count(acc,n):
    parts, count = help_parts(acc,n), 0
    while parts >= 1:
        count = count + help_count(get_all_sub_set(acc,parts),n)
        parts = parts -1
    return count

  # >>> count_coins(15)
  #   6
  #   >>> count_coins(10)
  #   4
  #   >>> count_coins(20)
  #   9
  #   >>> count_coins(100) # How many ways to make change for a dollar?
    242

coins=[1,5,10,25]

print(count(coins,100))


# t = get_all_sub_set([1,2,3,4,5,6,7,8,9],4)
#
# print(len(t))


