
def num_eights(x):
    def help(count,x):
        if (x//10 ==0):
            if (x!=8):
                return count
            else:
                return count+1
        else:
            last,left = x%10, x//10
            if (last ==8):
                return help(count+1,left)
            else:
                return help(count,left)
    return help(0,x)


def pingpong(m):
    container = [0] * m

    def help(container,n):
        container[0] = 1

        def help2(acc,index,flag,lastOfPre):
            while ((num_eights(index+1)==0 and (index+1)%8 !=0) and index<=m-1 ):
                if flag:
                    acc[index] = lastOfPre+1
                    lastOfPre =lastOfPre+1
                else:
                    acc[index] = lastOfPre - 1
                    lastOfPre = lastOfPre - 1
                index= index +1

            if (flag and index<=m-1):
                acc[index]= acc[index-1]+1
            elif(not flag and index <= m-1):
                acc[index]= acc[index-1]-1
            if (index+1< m):
                return help2(acc, index + 1, not flag, acc[index])
            else:
                return


        help2(container,1,True,1)

        print('help2 finished')
        print(container)

    help(container,m)

    return container[m-1]




# print(  pingpong(24))


def tool_1(n):
    end, first, left = n % 10,1, n // 10
    while (left > 10):
        left = left // 10
    first = left
    return (first, end)

a,b= tool_1(12349)

print(a)
print(b)



def missing_digits(n):

    def tool_1(n):
        end, first, left = n % 10, 1, n // 10
        while (left > 10):
            left = left // 10
        first = left
        return (first, end)

    first, end = tool_1(n)
    # 12456  12236
    def help(n,count,begin,end):
        if ((end == begin) and (begin == first)):
            return count
        elif(end== begin):
            n=n//10
            pre, curr = (n // 10) % 10, end
            if pre + 1 == curr:
                return help(n,count, begin, pre)
            else:
                return help(n,count + 1, pre, curr - 1)
        else:
            pre,curr = (n//10)%10 , end
            if (pre+1== curr or pre==curr):
                return help(n//10,count,first,pre)
            else:
                return help(n,count+1,pre,curr-1)

    begin,end= tool_1(n)
    return help(n,0,first,end)

print( missing_digits(1223468))


