#(1,2,3,4,5,6,7,8,9) get 4 numbers,

def help_sub_set_remove_last_right(acc):
    rec,i,count = [0]*(len(acc)-1),0,len(acc)
    while i<=count-2:
        rec[i]=acc[i]
        i=i+1
    return rec


    pass
#[[1], [2], [3], [4], [5]] ,6 => [[1,6], [2,6], [3,6], [4,6], [5,6]]
def help_f_num(acc_sub,n):
    count,i = len(acc_sub),0
    while i<= count-1:
        acc_sub[i]=help_set_add_one(acc_sub[i],n)
        i=i+1
    return acc_sub


# def help_set_add_one(acc,one):
#     rec,i,count=[0]* (len(acc)+1),0,len(acc)+1
#     while i<=count-1:
#         if i<count-1:
#             rec[i]=acc[i]
#         else:
#             rec[i]=one
#         i=i+1
#     return rec

def help_set_add_one(acc,one):
    rec,i,count=[0]* (len(acc)),0,len(acc)
    while i<=count-1:
        acc_item =acc[i]
        if(type(acc_item) == type(1)):
            temp= [0] * 2
            temp[0]= acc_item
            temp[1]=one
        else:
            temp, t_acount, t_i = [0] * (len(acc_item) + 1), len(acc_item), 0
            while t_i <= t_acount-1:
                temp[t_i] = acc_item[t_i]
                t_i = t_i + 1
            temp[t_acount] = one
        rec[i] = temp
        i = i + 1
    return rec


def help_subSet_subSet(sub1,sub2):
    acount,l1,l2,i = len(sub1)+len(sub2),len(sub1),len(sub2),0
    rec =[0] * acount
    while i<=acount-1:
        if i<= l1-1:
            rec[i]=sub1[i]
        else:
            rec[i]=sub2[i-l1]
        i= i+1
    return rec


def help_all_set_1(acc,n):
    if n==1:
        rec = [0] * len(acc)
        count,i =len(acc),0
        while(i<=count-1):
            rec[i]=[acc[i]]
            i= i+1
        return rec
    else:
        return []

def get_all_sub_set(arr,n):
    def help(arrSub,m):
        if m ==1:
            return help_all_set_1(arrSub,m)
        elif len(arrSub) == m:
            return [arrSub]
        else:
            nextArrSub,left= help_sub_set_remove_last_right(arrSub),arrSub[len(arrSub)-1]
            return help_subSet_subSet(help_set_add_one(help(nextArrSub,m-1),left),help(nextArrSub,m))
    return help(arr,n)



# t = get_all_sub_set([1,2,3,4,5,6,7,8,9],4)
#
# print(len(t))




# test step by steps

# t1= help_all_set_1([1,2,3,4,5],1)
#
# print(t1)
#
# t2 = help_set_add_one([[1,2],[2,4]],7)
#
# print(t2)
#
# t3= help_f_num([[1], [2], [3], [4], [5]],6)
#
# print(t3)
#
# t4 = help_sub_set_remove_last_right([1,2,3,4])
#
# print(t4)
#
# t5 =help_subSet_subSet([[1],[2],[3]],[[4],[5],6,7])
#
# print(t5)