
def count_Stair_ways(n):
    def help(m):
        if m ==1:
            return 1
        elif m==2:
            return 2
        else:
            return help(m-1)+help(m-2)
    return help(n-1)+ help(n-2)

# test = count_Stair_ways(3)
#
# print(test)

# """
#     >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
#     4
#     >>> count_k(4, 4)
#     8
#     >>> count_k(10, 3)
#     274
#     >>> count_k(300, 1) # Only one step at a time
#     1
#     """

# help function for count_k

# [1,2,3] ,2 =>[1,2]
def help_ok_set(acc,n):
    realCount,i,l,k=0,0,len(acc),0
    while i<= l-1:
        if acc[i]<=n:
            realCount = realCount+1
        i=i+1
    rec = [0]*realCount
    while k<= realCount-1:
        rec[k]=acc[k]
        k=k+1
    return rec


# n=3 =>[1,2,3]
def help_set_From_n(n):
    rec,i = [0]* n,0
    while i<=n-1:
        rec[i]=i+1
        i=i+1
    return rec


# print(help_set_From_n(4))
# print(help_ok_set([1,2,3],2))


def count_k(n, k):
    def help(okAcc,m):
        if (len(okAcc)==1 and okAcc[0] == m):
            return 1
        else:
            total,i,acount = len(okAcc),0,0
            while i<=total-1:
                isZero = m-okAcc[i]
                if isZero ==0:
                    acount = acount +1
                else:
                    acount = acount + help(help_ok_set(okAcc, m - okAcc[i]), m - okAcc[i])
                i = i+1
            return acount
    return help(help_set_From_n(k),n)

print(count_k(130,1))




def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [x*s[x] for x in range(0,len(s)-1) if x%2 ==0]

def help_first_layer():
    """
     [5,10,5,10,5],0 => [[5,5],[5,10],[5,5]]
     ==>[(0,2),(0,3),(0,4)]
    """
    pass

def help_next(i):
    pass

def help_left_list():
    pass

def help_left_list_first():
    pass

def help_set_extend_one_layer(arr,arr2):
    """
    [1,3] extend => [[1,3,5],[1,3,6],[1,3,7],[1,3,8],[1,3,9],[1,3,10],[1,3,11],[1,3,12]]
    """
    rec,count,i = [],len(arr2),0
    while i<= count-1:
        temp=arr[:]
        temp.append(arr2[i])
        rec.append(temp)
        i= i+1
    return rec


def help_set_extend(arr,currArr,rightIndex):
    rightArr=arr[rightIndex:]
    count = len(rightArr)
    if count >0:
        pass
    else:
        return currArr
def help_list_non_consecutive_elements(l,i):
    """
    [1,2,3,4,5,6,7,8,9,10,11,12],0 =>
    1 step :[ [1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],[1,10],[1,11],[1,12] ]  = first_layer
    2 step iterator the fist_layer to {extend} each item in first layer
      2.1:  [1,3] extend => [[1,3,5],[1,3,6],[1,3,7],[1,3,8],[1,3,9],[1,3,10],[1,3,11],[1,3,12]]
            [1,3,5] extend => [[1,3,5,7],[1,3,5,8],[1,3,5,9],[1,3,5,10],[1,3,5,11],[1,3,5,12]]
            [1,3,5,7] extend => [[1,3,5,7,9],[1,3,5,7,10],[1,3,5,7,11],[1,3,5,7,12]]
      2.2: core:  1: find the list[begin:]  2: extend the curr in []  3:recursive

    [5,10,5,10,5],0  =>[[5,5,5],[5,10],[5,5]]
    [5,10,5,10,5],1 =>[[10,10],[10,5]]
    [5,10,5,10,5],2 =>[[5,5]]
    [5,10,5,10,5],3=> [[10]]
    [5,10,5,10,5],4=>[[5]]
    """
    firstLayer= help_first_layer(l,i)
    pass



def help_max_from_array():
    pass

def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    count,i,maxValue= len(s),0,0
    while i<= count-1:
        arrCurr = help_list_non_consecutive_elements(s,i)
        maxCurr = help_max_from_array(arrCurr)
        if maxCurr>maxValue:
            maxValue=maxCurr
        i= i+1
    return maxValue







