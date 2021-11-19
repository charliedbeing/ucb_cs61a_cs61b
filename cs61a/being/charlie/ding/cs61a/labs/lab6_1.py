
def help_find_item(lst,entry,timers):
    i,total,count,index_result = 0,len(lst),0,0

    while i<= total-1:
        if lst[i]==entry:
            count = count+1
            if count == timers:
                index_result = i
                break
            i=i+1
        i =i+1
    return index_result

def help_entry_timers(lst,entry):
    result =0
    for item in lst:
        if item == entry:
            result=result+1
    return result

def insert_items(lst, entry, elem):
    i,count,timers = 1,help_entry_timers(lst,entry),0

    while i<=count:
        index = help_find_item(lst,entry,i)
        lst.insert(index+1,elem)
        i =i+1
    return lst


test =  insert_items([1,2,3,4,5,4,8,4],4,99)

print(test)
