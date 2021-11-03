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

# arr1 =[1,2,3,4,5,6,7,8,9,10,11,12]
# test = help_set_extend_one_layer([1,3],arr1[4:])
#
# print(test)

def help_set_extend_one_layer_2(arr,index,set):
    """
    [1,3] extend => [[1,3,5],[1,3,6],[1,3,7],[1,3,8],[1,3,9],[1,3,10],[1,3,11],[1,3,12]]
    """
    rec,count,i = [],len(set),index+2
    while i<= count-1:
        temp1,temp2=arr[:],arr[:]
        temp1.append((set[i],i))
        temp2.append((set[i]))
        rec.append((temp1,temp2))
        i= i+1
    return rec

# arr1 =[1,2,3,4,5,6,7,8,9,10,11,12]
# test = help_set_extend_one_layer_2([1],0,arr1)
#
# print(test)


def help_set_non_consecutive(arr,index):
    count =len(arr)-1
    def help(currArr,i):
        if i <= count-2:
            layerOne= help_set_extend_one_layer_2(currArr,i,arr)
            rec,layerOneCount,i =[],len(layerOne),0
            while i<= layerOneCount-1:
                itemWithIndex,item = layerOne[i]
                rec.append(help(item,itemWithIndex[len(itemWithIndex)-1][1]))
                i= i+1
            return rec
        else:
            return currArr
    return help([arr[0]],0)

def help_in_set(rec,arr):
    res=False
    for item in rec:
        if item == arr:
            res=True
            break
    if rec == arr:
        res = True
    return res




def help_append(rec,arr):
    if(not help_in_set(rec,arr)):
        if (type(arr[0]) == type([])):
            rec.append(arr[0])
        elif (type(arr[0]) == type(1)):
            rec.append(arr)
    return rec

def help_set_non_consecutive_2(arr,index):
    count =len(arr)-1
    def help(currArr,i):
        if i <= count-2:
            layerOne= help_set_extend_one_layer_2(currArr,i,arr)
            rec,layerOneCount,i =[],len(layerOne),0
            while i<= layerOneCount-1:
                itemWithIndex,item = layerOne[i]
                help_append(rec,help(item,itemWithIndex[len(itemWithIndex)-1][1]))
                i= i+1
            return rec
        else:
            return currArr
    return help([arr[index]],index)

def help_set_non_consecutive_3(arr,index):
    count =len(arr)-1
    rec=[]
    def help(currArr,i,acc):
        if i <= count-2:
            layerOne= help_set_extend_one_layer_2(currArr,i,arr)

            layerOneCount,i = len(layerOne),0
            while i<= layerOneCount-1:
                itemWithIndex,item = layerOne[i]
                help_append(acc,help(item,itemWithIndex[len(itemWithIndex)-1][1],acc))
                i= i+1
            return acc
        else:
            return currArr

    help([arr[index]], index, rec)
    return rec



# set =[1,2,3,4,5,6,7,8,9,10,11,12]
#
# set1 =[1,2,3,4,5,6,7]
#
# test = help_set_non_consecutive_3(set1,0)

# print(test)

def help_arr_sum(arr):
    count, i, res = len(arr), 0, 0
    while i<= count-1:
        res= res + arr[i]
        i=i+1
    return res

def help_arr_mul(arr):
    count, i, res = len(arr), 0, 1
    while i<= count-1:
        res= res * arr[i]
        i=i+1
    return res

def help_arr_mul_r(arr):
    if len(arr)==1:
        return arr[0]
    else:
        last = len(arr)-1
        return arr[last]*help_arr_mul_r(arr[:last])


# print(help_arr_mul_r([1,2,3,4]))


def help_sum_arr_max(arr):
    count,i,res,total= len(arr),0,0,0
    while i<= count-1:
        total = help_arr_sum(arr[i])
        if total >res:
            res = total
        i=i+1
    return res

def help_sum_max(f,arr):
    count,i,res,total= len(arr),0,0,0
    while i<= count-1:
        total = f(arr[i])
        if total >res:
            res = total
        i=i+1
    return res

aa=[[3, 5, 7], [3, 6], [3, 7]]

print(help_sum_max(help_arr_mul_r,aa))


def all_non_consecutives(arr):
    count,i,allMax = len(arr),0,[]
    while i<= count-1:
        temp = help_set_non_consecutive_3(arr,i)
        print(temp)
        allMax.append(help_sum_arr_max(temp))
        i =i+1
    return max(allMax)
#
# set1 =[1,2,3,4,5,6,7]
# test = all_non_consecutives(set1)
#
# print(test)




# def help_set_non_consecutive_r(arr,index):
#     count,rec =len(arr)-1,[]
#     def help(currArr,i):
#         if i <= count-2:
#             layerOne= help_set_extend_one_layer_2(currArr,i,arr)
#             layerOneCount,i =len(layerOne),0
#             while i<= layerOneCount-1:
#                 itemWithIndex,item = layerOne[i]
#                 rec.append(help(item,itemWithIndex[len(itemWithIndex)-1][1]))
#                 i= i+1
#             return rec
#         else:
#             return currArr
#     return help([arr[0]],0)


# List Comprehensions

def list_genergate():
    s=[x*x-3 for x in range(0,9) if x%2==1]
    s2=[(lambda x: 2+x)(x) for x in range(0,9) if x%2 ==0]
    print(s)
    print(s2)

list_genergate()


# nest and recursive is the basic tool for the structure, and the structure is the fundamental block or framework.
def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [x*s[x] for x in [x for x in [s.index(x) for x in s] if x%2==0]]






