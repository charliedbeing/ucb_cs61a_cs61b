
# > >> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
# > >> repeated(s, 2)
# 9
# > >> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
# > >> repeated(s2, 3)
# 8
# > >> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
# > >> repeated(s, 3)
# 2
# > >> repeated(s, 3)
# 5
# > >> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
# > >> repeated(s2, 3)
# 2


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

s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])

it = trans(s)

# for _ in range(1,12):
#     print(next(it))



def repeated(t, k):
    assert k > 1
    timers = 1

    def help(t,k):
        nonlocal timers
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

        value, timers_new = 0, 0

        while True:
            temp = next(new_t)
            if temp[1] == k:
                if timers == 1:
                    value = temp[0]
                    timers = timers + 1
                    break
                elif timers == 2:
                    timers_new = timers_new + 1
                    if timers_new == timers:
                        value = temp[0]
                        break

        return value


    return help


s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])

test1 = repeated(s,3)

print(test1)

test2 = repeated(s,3)


print(test2)





