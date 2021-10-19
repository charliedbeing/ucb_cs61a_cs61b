def merge(n1, n2):
    def removeZero(n):
        res=n
        while res%10 ==0 and res>0 :
            res = res//10
        return res
    def help(acc,n1,n2):
        n1,n2 = removeZero(n1),removeZero(n2)
        lastN1, leftN1,lastN2,leftN2,small =0,0,0,0,1
        if n1>0:
            lastN1,leftN1=n1%10, n1//10
        if n2>0:
            lastN2,leftN2 =n2%10,n2//10

        if(lastN1>0 and lastN2 >0):
            small = min(lastN1,lastN2)
        else:
            small= lastN1+lastN2
        if small>0:
            acc= acc+int.__str__(small)
            if small == lastN1:
                leftN2 =n2
            elif small ==lastN2:
                leftN1 = n1
        if (leftN1>0 or leftN2>0):
            return help(acc,leftN1,leftN2)
        else:
            return acc
    return help('',n1,n2)

test = merge(831,920)

print(test)