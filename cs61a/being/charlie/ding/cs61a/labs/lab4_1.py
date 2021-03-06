def paths(m, n):
    def help(curr, dest):
        if curr == dest:
            return 1
        elif curr[0]>dest[0] or curr[1]>dest[1]:
            return 0
        elif curr[0] + 1 <= dest[0] or curr[1] + 1 <= dest[1]:
            return help([curr[0] + 1, curr[1]], dest) + help([curr[0], curr[1] + 1], dest)


    return help([0, 0], [m - 1, n - 1])

# print(paths(1,157))

# 20125 =>[2,0,1,2,5]


def help_number_to_arr(n):
    def help(m,acc):
        if m<10:
            acc.append(m)
            return acc
        else:
            acc.append((m%10))
            return help(m//10,acc)
    return help(n,[])

# t1= 20125
# t2= help_number_to_arr(t1)
# t2.reverse()
# print(t2)



def help_merge_set_distinct(s1,s2):
    """
    merge set s1 and s2 and keep one item is there are two sames
    """
    pass

def help_copy_set_add_value(acc,n):
    rec=acc[:]
    rec.append(n)
    return rec

def help_branch_deal(arr,n):
    finalLen,rec = n,[]
    def help_acc(acc,arr,n):
        resL,currL =len(acc),len(arr)
        if resL ==finalLen:
            return acc
        elif currL ==n:
            acc.extend(arr)
            return acc
        elif resL < finalLen:
            while len(arr)>=n-1:
                rec.append(help_acc(help_copy_set_add_value(acc,arr[0]),arr[1:],n-1))
                arr= arr[1:]

        else:
            return []

    help_acc([], arr, n)
    return rec


def help_branch_deal_2(arr,n):

    finalLen,rec = n,[]
    def help_acc(acc,arr,n):
        resL,currL =len(acc),len(arr)
        if resL ==finalLen:
            return acc
        elif currL ==n:
            acc.extend(arr)
            return acc
        elif resL < finalLen:
            while len(arr)>=n-1:
                rec.append(help_acc(help_copy_set_add_value(acc,arr[0]),arr[1:],n-1))
                arr= arr[1:]

        else:
            return []

    while len(arr)>=n:
        rec.append(help_acc([arr[0]],arr[1:],n-1))
        arr=arr[1:]

    return rec


def help_branch_deal(arr,n):
    rec,finalLen=[],n

    def help_branch_deal_3(acc, arr, n):

        def help_acc(acc, arr, n, finalLen):
            resL, currL = len(acc), len(arr)
            if resL == finalLen:
                return acc
            elif currL == n:
                acc.extend(arr)
                return acc
            elif resL < finalLen and n-1>=0:
                temp=[]
                while len(arr)>=n:
                    temp.append(help_branch_deal_3(help_copy_set_add_value(acc, arr[0]),arr[1:],n-1))
                    arr=arr[1:]
                return temp

            else:
                return []

        while len(arr) >= n:
            rec.append(help_acc(help_copy_set_add_value(acc, arr[0]), arr[1:], n - 1,finalLen))
            arr = arr[1:]

    help_branch_deal_3([],arr,n)

    return rec


# test = help_branch_deal([2, 0, 1, 2, 5], 3)
# print(test)


def help_sub_seqshelp_sub_seqs(m, k):
    if len(m) == k:
        return m
    else:
        length, i, temp = len(m), 0, []
        while i >= length - k - 1:
            temp = help_merge_set_distinct(temp, help_branch_deal(m[i:], k))
        return temp

def max_subseq(n, t):
    rec,arr =[],help_number_to_arr(n)
    arr.reverse()
    while t>=1:
        rec.extend(help_sub_seqshelp_sub_seqs(arr,t))
        t =t-1
    return rec

# test = max_subseq(20125,3)
#
# print(test)

def help_word_acc_state(w):
    """
    word to [(False,'w'),(False,'o'),(),()]
    """
    count, i, rec = len(w), 0, []
    while i <= count - 1:
        rec.append((True,w.__getitem__(i)))
        i = i + 1
    return rec


def help_word_acc(w):
    """
    word to ['w','o','r','d']
    """
    count,i,rec =len(w),0,[]
    while i<= count-1:
        rec.append(w.__getitem__(i))
        i=i+1
    return rec

# test = help_word_acc("hello")
# print(test)
#
# test = help_word_acc_state("hello")
# print(test)

def help_compare(c,arr):
    count,i = len(arr),0
    while i<= count-1:
        flag,letter = arr[i]
        if flag:
            if letter == c:
                arr[i]=(False,c)
                break
            else:
                i=i+1
        else:
            i =i+1

def help_arr_str(arr):
    count,i,res= len(arr),0,''

    while i<= count-1:
        flag,c = arr[i]
        if flag:
            res= res +c
            i=i+1
        else:
            i = i + 1
    return res




def add_chars(w1, w2):
    """
    "coy", "cacophony", => acphon
    """
    arr1,arr2 = help_word_acc(w1),help_word_acc_state(w2)
    def help(arr1):
        if len(arr1)>0:
            c,left = arr1[0],arr1[1:]
            help_compare(c,arr2)
            return help(left)

    help(arr1)
    return help_arr_str(arr2)

t = add_chars('coy','cacophony')

print(t)


