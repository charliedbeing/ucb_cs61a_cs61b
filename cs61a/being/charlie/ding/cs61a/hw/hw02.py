def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    """
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
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    """
    container = [0] * m
    def help(container, n):
        container[0] = 1
        def help2(acc, index, flag, lastOfPre):
            while ((num_eights(index + 1) == 0 and (index + 1) % 8 != 0) and index <= m - 1):
                if flag:
                    acc[index] = lastOfPre + 1
                    lastOfPre = lastOfPre + 1
                else:
                    acc[index] = lastOfPre - 1
                    lastOfPre = lastOfPre - 1
                index = index + 1

            if (flag and index <= m - 1):
                acc[index] = acc[index - 1] + 1
            elif (not flag and index <= m - 1):
                acc[index] = acc[index - 1] - 1
            if (index + 1 < m):
                return help2(acc, index + 1, not flag, acc[index])
            else:
                return
        help2(container, 1, True, 1)

    help(container, m)

    return container[m - 1]


 # >>> missing_digits(4) # No missing numbers between 4 and 4
    # 0
    # True

def missing_100digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    """
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
    if n<10:
        return 0
    else:
        return help(n, 0, first, end)



def next_largest_coin(coin):
    """Return the next coin.
    >>> next_largest_coin(1)
    5
    >>> next_largest_coin(5)
    10
    >>> next_largest_coin(10)
    25
    >>> next_largest_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25

def count_coins(total):
    """Return the number of ways to make change for total using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    """
    "*** YOUR CODE HERE ***"