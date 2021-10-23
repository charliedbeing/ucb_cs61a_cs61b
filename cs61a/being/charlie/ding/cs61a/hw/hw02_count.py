# acc=[1,5,10,25] n =100   all possible composes  sum (number in acc ) = 100
def help_parts(acc,n):
    index =0
    while acc[index]<= n:
        index = index +1
    return index

def help_partition_set(acc,index):
    rec,i=[0]*index,0
    while(i<=index-1):
       rec[i] = acc[i]
    return rec



def help_set_left_sum(acc):
    # acc=[1,5,10,25] return 1+5+10
    total,index,i = 0,len(acc)-1,0
    while i<= index:
        total = total +acc[i]
    return total


def help_set_max(acc):
    # acc=[1,5,10,25] return 25
    index = len(acc)-1
    return acc[index]

def help_set_remove_max(acc):
    # acc=[1,5,10,25] return [1,5,10]; acc=[1,5,10] return [1,5]
    return help_partition_set(acc,1)




# return the count of solutions. partition
def help(setNumbers,total):
    if len(setNumbers) ==1:
        return 1
    else:
        maxTimes = (total - help_set_left_sum(setNumbers))//help_set_max(setNumbers)
        temp,index=0,1
        while maxTimes>=1:
            curr,left = help_set_max(setNumbers),help_set_remove_max(setNumbers)
            temp = temp + help(left,total-curr * index)
        return temp



def count(acc,n):
    parts, count = help_parts(acc,n)+1, 0
    while parts >= 1:
        count = count + help(help_partition_set(acc,parts),n)
        parts = parts -1
    return count





