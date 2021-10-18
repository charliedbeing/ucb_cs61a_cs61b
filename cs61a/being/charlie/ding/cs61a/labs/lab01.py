def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    total,index = 1,k
    while index>0:
        total = total * n
        n,index = n-1,index-1
    return total


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    total,work =0,y
    while work>0:
        total = total + work % 10
        work = work // 10
    return total + work

def sum_digits_r(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    def help(index,acc=0):
        if index//10 >0:
            return help(index//10,acc+index%10)
        else:
            return index +acc
    return help(y)


# test WWPD

def bake(cake,make):
    """ test varable will referent new value
    >>> bake(0,29)
    1
    29
    29
    >>> bake(2,'charlie')
    2

    """
    if cake == 0:
        cake = cake + 1
        print(cake)
    if cake == 1:
        print(make)
    else:
        return cake
    return make


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(80808080)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    result,work = False,n
    while work>0:
        if work<10:
            break
        else:
            left, curr = work // 10, work % 10
            if curr == 8:
                if left % 10 == 8:
                    result = True
                    break
                else:
                    work = left
            else:
                work = left

    return result


