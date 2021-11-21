def make_bank(balance):
    """Returns a bank function with a starting balance. Supports
    withdrawals and deposits.

    >>> bank = make_bank(100)
    >>> bank('withdraw', 40)    # 100 - 40
    60
    >>> bank('hello', 500)      # Invalid message passed in
    'Invalid message'
    >>> bank('deposit', 20)     # 60 + 20
    80
    >>> bank('withdraw', 90)    # 80 - 90; not enough money
    'Insufficient funds'
    >>> bank('deposit', 100)    # 80 + 100
    180
    >>> bank('goodbye', 0)      # Invalid message passed in
    'Invalid message'
    >>> bank('withdraw', 60)    # 180 - 60
    120
    """
    def bank(message, amount):
        nonlocal balance
        if message == 'withdraw':
            if amount> balance:
                return 'Insufficient funds'
            balance = balance-amount
            return balance
        elif message == 'deposit':
            balance = balance+ amount
            return balance
        else:
            return 'Invalid message'

    return bank

def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Frozen account. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Frozen account. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    try_times,acc_try_times =0,[]
    def help(amount,opencode):
        nonlocal balance, try_times
        if len(acc_try_times)==3:
            return "Frozen account. Attempts: "+str(acc_try_times)
        else:
            if opencode == password:
                if amount <= balance:
                    balance = balance - amount
                    return balance
                else:
                    return 'Insufficient funds'
            else:
                acc_try_times.append(opencode)
                return 'Incorrect password'
    return help




# """Return the first value in iterator T that appears K times in a row. Iterate through the items such that
#    if the same iterator is passed into repeated twice, it continues in the second call at the point it left off
#    in the first.
#
#    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
#    >>> repeated(s, 2)
#    9
#    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
#    >>> repeated(s2, 3)
#    8
#    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
#    >>> repeated(s, 3)
#    2
#    >>> repeated(s, 3)
#    5
#    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
#    >>> repeated(s2, 3)
#    2
#    """

timers=1
def repeated(t, k):
   
    nonlocal timers
    assert k > 1
    def help(timers):

        def trans(t):
            pre = -1
            curr_single, curr = next(t), (0, 0)
            while True:
                if pre < 0:
                    curr = (curr_single, 1)
                    pre = curr_single
                else:
                    if pre == curr_single:
                        curr = (curr[0], curr[1] + 1)
                        pre = curr[0]
                    else:
                        curr = (curr_single, 1)
                        pre = curr_single
                curr_single = next(t)
                yield curr

        new_t = trans(t)

        value,timers_new = 0,0

        while True:
            temp = next(new_t)
            if temp[1] == k:
                if timers ==1:
                    value = temp[0]
                    timers = timers+1
                    break
                elif timers == 2:
                    timers_new = timers_new + 1
                    if timers_new == timers:
                        value = temp[0]
                        break

        return value

    timers =1
    return help(timers)




