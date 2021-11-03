def skip_add(n):
    """ Takes a number n and returns n + n-2 + n-4 + n-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    """

    if n ==0 :
        return 0
    elif n-2>=0 or n-2==-1:
        return n + skip_add(n-2)
    else:
        return 0

def summation(n, term):

    """Return the sum of the first n terms in the sequence defined by term.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    """
    assert n >= 1
    if n==1:
        return term(n)
    else:
        return term(n)+summation(n-1,term)


def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """

    def help(curr, dest):
        if curr == dest:
            return 1
        elif curr[0] > dest[0] or curr[1] > dest[1]:
            return 0
        elif curr[0] + 1 <= dest[0] or curr[1] + 1 <= dest[1]:
            return help([curr[0] + 1, curr[1]], dest) + help([curr[0], curr[1] + 1], dest)

    return help([0, 0], [m - 1, n - 1])


def max_subseq(n, t):
    """
    Return the maximum subsequence of length at most t that can be found in the given number n.
    For example, for n = 20125 and t = 3, we have that the subsequences are
        2
        0
        1
        2
        5
        20
        21
        22
        25
        01
        02
        05
        12
        15
        25
        201
        202
        205
        212
        215
        225
        012
        015
        025
        125
    and of these, the maxumum number is 225, so our answer is 225.

    >>> max_subseq(20125, 3)
    225
    >>> max_subseq(20125, 5)
    20125
    >>> max_subseq(20125, 6) # note that 20125 == 020125
    20125
    >>> max_subseq(12345, 3)
    345
    >>> max_subseq(12345, 0) # 0 is of length 0
    0
    >>> max_subseq(12345, 1)
    5
    """
    "*** YOUR CODE HERE ***"


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
    Return a string containing the characters you need to add to w1 to get w2.

    You may assume that w1 is a subsequence of w2.

    >>> add_chars("owl", "howl")
    'h'
    >>> add_chars("want", "wanton")
    'on'
    >>> add_chars("rat", "radiate")
    'diae'
    >>> add_chars("a", "prepare")
    'prepre'
    >>> add_chars("resin", "recursion")
    'curo'
    >>> add_chars("fin", "effusion")
    'efuso'
    >>> add_chars("coy", "cacophony")
    'acphon'
    """
    arr1, arr2 = help_word_acc(w1), help_word_acc_state(w2)

    def help(arr1):
        if len(arr1) > 0:
            c, left = arr1[0], arr1[1:]
            help_compare(c, arr2)
            return help(left)

    help(arr1)
    return help_arr_str(arr2)