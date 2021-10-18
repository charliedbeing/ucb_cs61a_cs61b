def assignmentStatements():
    x =10
    y=x
    x=20
    # x= y+1 # x = 11
    # y= x-1  # y =10
    # assert y == 10,'some thing is wrong'
    # very trick place:
    x,y = y+1, x-1
    assert x ==11 and y == 19 , 'this is good example to show: Firstly evaluate all on right side,Secondly binding them'
    # if there are more than one name/expression in the statement,evaluate all the expressions first from left to right
    # after finishing all the evaluating work at right side, and then assignment begin or begin to bind
assignmentStatements()

#f1
def f(x):
    return x+1

#f2
def f(z):
    return z+2

# f3
def f(z,y=10):
    return z+y+2

# we can see that python environment use f3 overwrite f2 ,since they have same function name ,since they have different param list
assert f(2) == 14 ,'function name is the first important'

assert f(1,2) ==5 ,'function name is same but param list is not same, not just param name is not'

# not None == True
def wwpd_lambdaTheFree():
    x = None
    print(type(x))
    print(x)
    if not x:
        print('None is not change to boolean')
    # lambda function have no intrinsic name ,so if we want to call it, use this way
    isFunction = (lambda: 10)
    print(type(print)) # function
    print(type(isFunction))
    y= (lambda: 3)()
    print(y)


wwpd_lambdaTheFree()

def wwpd_lambdaTheFree_2():
    b = lambda x: lambda : x
    c = b(111)
    print(type(c))
    print(c)
    print(c())

    # step 2
    # show how to call lambda and how to input param from outside.
    bb = lambda x: x+ (lambda y: y+ 10* x)(x)

    t1 = bb(10)

    print('--------')
    print(type(t1))


wwpd_lambdaTheFree_2()


def wwpd_lambdaTheFree_3():
    d = lambda f: f(4)

    def square(x):
        return x*x
    test = d(square)
    print(type(test))
    print(test)

print('----wwpd_lambdaTheFree_3----')
wwpd_lambdaTheFree_3()

def wwpd_lambdaTheFree_4():
    z=3
    e= lambda x: lambda y: lambda: x+y+z

    test = e(1)(2)
    print(type(test))
    print(test())
   # print(test(111))  # TypeError: <lambda>() takes 0 positional arguments but 1 was given
print('---wwpd_lambdaTheFree_4----')
wwpd_lambdaTheFree_4()

def wwpd_lambdaTheFree_5():
    higher_order_lambda = lambda f: lambda x: f(x)
    g= lambda x: x* x
    # higher_order_lambda(2)(g) #TypeError: 'int' object is not callable
    print(higher_order_lambda(g)(5))

    call_three = lambda f: lambda x: f(f(f(x)))

    print(call_three(g)(2) == pow(2,6))
    print(call_three(g)(2))

    print_lambda = lambda z: print(z)

    print(print_lambda(2))

wwpd_lambdaTheFree_5()

# 
#
#
def applyFnToAbs(f):
    def help(y):
        if y<0:
            return f(-y)
        else:
            return f(y)
    return help

testFn = applyFnToAbs(lambda x:2*x+1)

print(testFn(-10))



