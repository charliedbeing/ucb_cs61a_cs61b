def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    def help(acc,x,y):
        if y==0:
            return acc
        else:
            return help(acc+x,x,y-1)
    return help(0,5,3)

def multiply2(m,n):
    """
    >>> multiply(5, 3)
    15
    """
    if n>0:
        return  m+ multiply2(m,n-1)
    return 0

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    def help(count,n):
        print(n)
        if n == 1:
            return count
        elif(n%2==0):
            return help(count+1,n//2)
        else:
            return help(count+1,3*n+1)

    return help(1,n)

def merge(n1, n2):
    """ Merges two numbers
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
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
            acc= int.__str__(small)+acc
            if small == lastN1:
                leftN2 =n2
            elif small ==lastN2:
                leftN1 = n1
        if (leftN1>0 or leftN2>0):
            return help(acc,leftN1,leftN2)
        else:
            return int(acc)
    return help('',n1,n2)

def make_func_repeater(f, x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    """
    def help(acc,f,x):
        if (x==0):
            return acc
        else:
            return help(f(acc),f,x-1)
    return lambda y: help(y,f,x)


def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    >>> is_prime(17)
    True
    """
    def help(k):
        if k>0:
            if (k == 1):
                return True
            elif (n % k == 0):
                return False
            else:
                return help(k - 1)
        else:
            return False
    return help(n-1)

