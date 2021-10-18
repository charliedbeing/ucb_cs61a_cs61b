# def cycle(f1, f2, f3):
#     def help(x):
#         def help2(y):
#             def lessOrEqualThree():
#                 if (x <= 3):
#                     if (x == 0):
#                         return lambda:y
#                     elif (x == 1):
#                         return lambda: f1(y)
#                     elif (x == 2):
#                         return lambda: f2(f1(y))
#                     elif (x == 3):
#                         return lambda : f3(f2(f1(y)))
#             if (x <= 3):
#                 return lessOrEqualThree()()
#         return help2
#     return help
#
#
# def add1(x):
#     return x + 1
#
# def times2(x):
#      return x * 2
#
# def add3(x):
#     return x + 3

# my_cycle = cycle(add1, times2, add3)
#


# print(type(my_cycle))
#
# print(my_cycle(0)(9))
#
# print(my_cycle(1)(9))
#
# print(my_cycle(3)(9))


###
def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5

    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    def help(x):
        def help2(y):
            def lessOrEqualThree():
                if (x <= 3):
                    if (x == 0):
                        return lambda:y
                    elif (x == 1):
                        return lambda: f1(y)
                    elif (x == 2):
                        return lambda: f2(f1(y))
                    elif (x == 3):
                        return lambda : f3(f2(f1(y)))
            if (x <= 3):
                return lessOrEqualThree()()
            else:
                count, acc = 4, f3(f2(f1(y)))
                while count <= x:
                    temp = count % 3
                    if (temp ==1):
                        acc = f1(acc)
                        count = count + 1
                    elif(temp ==2):
                        acc=f2(acc)
                        count = count + 1
                    elif(temp==0):
                        acc=f3(acc)
                        count = count + 1
                return acc
        return help2
    return help


