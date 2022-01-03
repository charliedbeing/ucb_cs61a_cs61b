from lab07 import *



def sequences_list():
    lst =[1,2,3,4,5]
    print(lst[1:3])
    print(lst[0:len(lst)])
    print(lst[-4:])
    print(lst[3:])
    print(lst[1:4:2])
    print(lst[1:3:2])
    print(lst[:4:2])
    print(lst[1::2])
    print(lst[::-1])
    # print(lst +100)
    lst3 = [[1],[2],[3]]
    lst4 =[[[[[100]]]]]
    print(lst+lst3)
    print(lst+lst4)

# sequences_list()

# 1.3
def map_mut(f, L):
    i,count = 0, len(L)
    while i<= count -1:
        temp = L[i]
        L[i] = f(temp)
        i = i +1

def test_map_mut():
    L = [1,2,3,4]
    map_mut(lambda x: x**2, L)
    print(L)

# test_map_mut()

# 1.4
def copy_list():
    L = [1, 2, 3, 4]
    p=L  #
    # p[1] =100
    # print(L)
    pp = L[:]
    print(pp)
    pp[1]=-100
    print(pp)
    print(L)

# copy_list()

# 2.3

def mutable_type():
    # a =1
    # b=2
    # dt = {a:12, b:2}
    a ='ddd'
    b=['d']  # unhashable type 'list'
    dt = {a:1,b:2}

# mutable_type()

# 2.4
def example_list():
    a = [1,[2,3],4]
    c = a[1]
    print(c)
    a.append(c) # here is shallow copy, reference level not value level
    print(a)
    c[0]=0
    print(c)
    print(a)

    a.extend(c)
    print(a)
    c[1]=9
    print(a)

    list1 =[1,2,3]
    list2 =[1,2,3]
    print(list1 == list)
    print(list1 is list2)


# example_list()

# 2.5  append extend and +
def distince_operator_in_list():
    a =[1,2,3,4]
    b= [10,20,30]

    a.append(b)
    b[0] =-1

    print(a)

    a.extend(b)
    print(a)
    b[0]= -2
    print(a)

    c= a+b

    print(a)
    print(c)
    d = c +[x for x in range(1,5,2)]
    print(d)

    aa = [1,2,[3,4],5]
    bb= aa[:] # just one layer deep copy, not fully deep copy
    bb[1] =6
    bb[2][0] =-3

    print(aa)



# distince_operator_in_list()

# 3.2
"""
36: 1,2,3,4,6,9,12,18,36
24: 1,2,4,6,12,24
"""
def gcd(a,b):
    def help_all_facotrs(n):
        rec =[]
        for i in range(1,n+1):
            if n% i == 0:
                rec.append(i)
        return rec

    def help_in_arr(arr1,arr2):
        rs = False
        i ,count = 0, len(arr1)
        while i <= count -1:
            if arr2.__contains__(arr1[i]):
                rs = True
                break
            else:
                i = i + 1
        return rs


    rs =1
    acc_short, acc_long,acc_i = help_all_facotrs(a),help_all_facotrs(b),[]
    acc_i = acc_short
    if len(acc_short) > len(acc_long):
        acc_i = acc_long
        acc_long = acc_short

    i,count = 0, len(acc_i)

    while i<= count -1:
        if acc_long.__contains__(acc_i[i]):
            if not help_in_arr(acc_i[i+1:] ,acc_long):
                return acc_i[i]
            else:
                i = i+1
        else:
            i = i+1


def test_gcd():
    t = gcd(24,30)
    print(t)

# test_gcd()


class Rational_Den(Exception):
    def __init__(self,message):
        self.message = message


def rational(num,den):
    if den == 0:
        raise Rational_Den('den can not be zero')
    else:
        return [num,den]

def numer(x):
    return x[0]

def denom(x):

    return x[1]

def simplify(f1):
    g = gcd(f1[0],f1[1])
    return rational(numer(f1)//g,denom(f1)//g)

def multiply(f1,f2):
    r = rational(numer(f1) * numer(f2), denom(f1)* denom(f2))
    return simplify(r)

def test_abstraction_barrier():
    x = rational(1,0)
    y = rational(7,11)
    t = multiply(x,y)
    print(t)
# secret message: you are amazing!!!!!!!!!!!!!!!!!!!! very cool man
# test_abstraction_barrier()

# 4 Tree
def tree(label,branches=[]):
    for b in branches:
        assert is_tree(b), 'branches must be trees'
    return [label] + list(branches)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for b in branches(tree):
        if not is_tree(b):
            return False
    return True

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return len(branches(tree)) == 0

def update_tree(tree,v):
    tree[0] = v


def test_tree():
    t1 = tree(1,[tree(2,[tree(3,[tree(4)])]),tree(100)])
    print(t1)

# test_tree()

def is_min_heap(t):
    rs = True
    def help(t):
        nonlocal rs
        if not is_leaf(t):
            curr,bs = label(t),branches(t)
            for branch in bs:
                if curr > label(branch):
                    rs = False
                    return
                else:
                    help(branch)

    help(t)

    return rs

def test_is_min_heap():
    t = tree(1,[tree(5,[tree(7)]),tree(3,[tree(9),tree(2)]),tree(6)])

    print(is_min_heap(t))

# test_is_min_heap()

def largest_product_path(tree):
    max_path = 0

    def help_tools_multiple(arr):
        rs = 1
        for i in arr:
            rs = rs * i
        return rs

    def help(t,acc=[]):
        nonlocal max_path
        if is_leaf(t):
            acc.append(label(t))
            max_path = max(max_path, help_tools_multiple(acc))
        else:
            curr,bs = label(t),branches(t)
            acc.append(curr)
            for branch in bs:
                temp =acc[:]
                help(branch,temp)

    help(tree)
    return max_path

def test_largest_product_path():
    t = tree(3,[tree(7,[tree(2)]),tree(8,[tree(1)]),tree(4)])
    print(largest_product_path(t))

# test_largest_product_path()

def contains(t,e):
    rs = False
    def help(t,e):
        nonlocal rs
        if is_leaf(t):
            if label(t) == e:
                rs = True
                return
        else:
            curr,bs = label(t), branches(t)
            if curr == e:
                rs = True
                return
            for branch in bs:
                help(branch,e)
    help(t,e)
    return rs

def test_contains():
    t = tree(3, [tree(7, [tree(2)]), tree(8, [tree(1)]), tree(4)])
    print(contains(t,15))

# test_contains()

def max_tree(t):
    def help(t):
        acc = 0

        def help_(t):
            nonlocal acc
            if is_leaf(t):
                if label(t) > acc:
                    acc = label(t)
            else:
                curr, bs = label(t), branches(t)
                if curr > acc:
                    acc = curr
                for branch in bs:
                    help_(branch)

        help_(t)
        return acc

    if not is_leaf(t):
        curr_max,bs = help(t),branches(t)
        update_tree(t,curr_max)
        for branch in bs:
            max_tree(branch)

def test_max_tree():
    t = tree(1, [tree(5, [tree(7)]),tree(3,[tree(9),tree(4)]),tree(6)])
    max_tree(t)

    print(t)

# test_max_tree()


def help(t):
    acc = 0
    def help_(t):
        nonlocal  acc
        if is_leaf(t):
            if label(t) > acc:
                acc = label(t)
        else:
            curr, bs = label(t), branches(t)
            if curr > acc:
                acc = curr
            for branch in bs:
                help_(branch)
    help_(t)
    return acc



def test_help():
    t = tree(1, [tree(5, [tree(7)]), tree(3, [tree(9), tree(4)]), tree(6)])
    t1= tree(3, [tree(9), tree(14)])
    print(help(t1))

# test_help()

def max_tree_2(t):
    if is_leaf(t):
        return t
    else:
        new_branches = [max_tree_2(branch) for branch in branches(t)]
        new_label = help(t)
        return tree(new_label,new_branches)

def test_max_tree_2():
    t = tree(1, [tree(5, [tree(7)]), tree(3, [tree(9), tree(4)]), tree(6)])
    t1 = max_tree_2(t)
    print(t1)

# test_max_tree_2()

def help_tool_remove_empty(arr):
    rs =[]
    for item in arr:
        if len(item)>0:
            rs.extend(item)
    return rs


def level_order(t):
    rec = [label(t)]
    def help(layer):
        if len(layer) > 0:
            curr_l, next_l = [label(x) for x in layer], help_tool_remove_empty([branches(x) for x in layer])
            rec.append(curr_l)
            help(next_l)

    help(branches(t))

    return rec

def test_level_order():
    t = tree(1, [tree(5, [tree(7,[tree(8)])]), tree(3, [tree(9), tree(4,[tree(14)])]), tree(6)])
    print(level_order(t))

# test_level_order()

def all_paths(t):
    rec =[]
    def help(t,acc=[]):
        if is_leaf(t):
            acc.append(label(t))
            rec.append(acc)
        else:
            curr,bs = label(t),branches(t)
            acc.append(curr)
            for branch in bs:
                temp = acc[:]
                help(branch,temp)
    help(t)
    return rec

def test_all_paths():
    t = tree(1, [tree(5, [tree(7, [tree(8)])]), tree(3, [tree(9), tree(4, [tree(14)])]), tree(6)])
    print(all_paths(t))

# test_all_paths()

# 5 Nonlocal

def make_max_finder():
    rec =[]
    def help(arr):
        nonlocal rec
        rec.extend(arr)
        return max(rec)
    return help

def test_make_max_finder():
    m = make_max_finder()
    print(m([5,6,7]))
    print(m([1,2,3]))
    print(m([9]))
    m2 = make_max_finder()
    print(m2([11,9]))
    print(m2([1,2,3,4]))


# test_make_max_finder()


x =5
def f(x):
    def g(s): # 1 here, the x from f(x) will cover the x from globe environment
        def h(h):
            nonlocal x # 4 here x is the same with #3 and the same with #2
            x= x +h
            return x
        nonlocal x  # 3 here  since the nonlocal statement, x is  the same with #2
        x = x+x     # x -> 7+7 = 14
        return h
    print(x)  # 2 here x = from the param in f(x) received  ->7
    return g


x = 5
"""
 485 nonlocal x  # 3 here  since the nonlocal statement, x is  the same with #2
 this example demonstrate that nonlocal variable  should be belong a function, 
 which can be at param or the scope of functions
"""

# def f_(z):
#     def g(s): # 1 here, the x from f(x) will cover the x from globe environment
#         def h(h):
#             nonlocal x # 4 here x is the same with #3 and the same with #2
#             x= x +h
#             return x
#         nonlocal x  # 3 here  since the nonlocal statement, x is  the same with #2
#         x = x+x     # x -> 7+7 = 14
#         return h
#     print(x)  # 2 here x = from the param in f(x) received  ->7
#     return g

def test_f_g_h():
    t =f(8)
    # t = f(7)(8)(9)
    # print(t == 19)
    # print(t)
    # t = f_(7)
    # print(t)

# test_f_g_h()

# 6 OOP
class Foo():
    x = 'bam'
    def __init__(self,x):
        self.x = x
    def baz(self):
        return self.x

class Bar(Foo):
    x = 'boom'
    def __init__(self,x):
        Foo.__init__(self,'er'+x)
    def baz(self):
        return Bar.x + Foo.baz(self)


def test_6_Foo_Bar():
    foo = Foo('boo')
    print(Foo.x)
    print(foo.x)
    print(foo.baz())
    # print(Foo.baz())
    print(Foo.baz(foo))

    bar = Bar('ang')
    print(Bar.x) # boom
    print(bar.x) # erang
    print(bar.baz()) #boomerang

# test_6_Foo_Bar()

class Student:
    def __init__(self,subjects):
        self.current_units =16
        self.subjects_to_take = subjects
        self.subjects_learned ={}
        self.partner = None
    def __str__(self):
        return 'my subjects:'
    def learn(self,subject,units):
        print('I just learned about '+ subject)
        self.subjects_learned[subject]=units
        self.current_units -= units

    def make_friends(self):
        if len(self.subjects_to_take) > 3:
            print('Whoa! I need more help!')
            self.partner = Student(self.subjects_to_take[1:])
        else:
            print("I'm on my own now!")
            self.partner = None

    def take_course(self):
        course = self.subjects_to_take.pop()
        self.learn(course,4)
        if self.partner:
            print('I need to switch this up!')
            self.partner = self.partner.partner
            print(self.partner)
            if not self.partner:
                print('I have failed to make a friend:(')

def test_Student():
    tim = Student(['CS61A','CS70','Chem1A','Bio1B','CogSci1'])
    tim.make_friends() # tim.partner => Student(['CS70','Chem1A','Bio1B','CogSci1'])

    print(tim.subjects_to_take)
    tim.partner.make_friends() # tim.partner.partner => Student(['Chem1A','Bio1B','CogSci1'])
    tim.take_course()
    tim.partner.take_course()
    tim.take_course()



# test_Student()

class Cat():
    noise = 'meow'
    def __init__(self,name):
        self.name = name
        self.hungry = True

    def meow(self,message=''):
        if self.hungry:
            print(self.noise+', '+self.name +' is hungry'+'\r\n'+message)
        else:
            print(Cat.noise+', '+'my name is '+ self.name+'\r\n'+message)

    def eat(self):
        print(self.noise)
        self.hungry= False

class Kitten(Cat):
    noise ="i'm baby"
    def __init__(self,name,mama):
        Cat.__init__(self,name)
        self.mama = mama

    def meow(self):
        Cat.meow(self,'I want mama '+ self.mama.name)

    def eat(self):
        Cat.eat(self)

def test_Cat_Kitten():
    cat = Cat('Tuna')
    kitten = Kitten('Fish',cat)
    cat.meow()
    kitten.meow()
    cat.eat()
    cat.meow()
    kitten.eat()
    kitten.meow()

# test_Cat_Kitten()

# 7 Object Oriented Trees

def filter_tree(t,fn):
    bs = t.branches

    def help(t,fn):
        if Tree.is_leaf(t):
            if not fn(t.label):
                t.remove=True
        else:
            curr,bs = t.label,t.branches
            if not fn(curr):
                t.remove = True
            else:
                for branch in bs:
                    help(branch,fn)

    for branch in bs:
        help(branch,fn)

    Tree.update_remove(t)






def test_7_filter_tree():
    t = Tree(1,[Tree(2),Tree(3,[Tree(4)]),Tree(6,[Tree(7)])])
    filter_tree(t,lambda x: x%2 !=0)

    print(t)


# test_7_filter_tree()


def nth_level_tree_map(fn,tree,n):
    tree.update_level()

    def help(t,fn,n):
        if Tree.is_leaf(t):
            if t.level == n:
                t.update(fn(t.label))
        else:
            curr,bs = t.label, t.branches
            if t.level == n:
                t.update(fn(t.label))
                for branch in bs:
                    help(branch,fn,n)
            else:
                for branch in bs:
                    help(branch,fn,n)
    help(tree,fn,n)
    print(tree)





def test_nth_level_tree_map():
    t = Tree(1, [Tree(2), Tree(3, [Tree(4)]), Tree(6, [Tree(7)])])
    nth_level_tree_map(lambda x: x*2, t,2)


# test_nth_level_tree_map()

# 8 Linked List

def has_cycle(link):
    count,select_one = False,link
    def help(link):
        nonlocal count,select_one
        if not link == Link.empty:
            if select_one == link:
                count = True
                return
            else:
                help(link.rest)
    help(link.rest)
    return count

def has_cycle_2(link):
    flag,is_cycle = link,False
    def help(link):
        nonlocal flag,is_cycle
        if not link == Link.empty:
            if link == flag:
                is_cycle = True
                return
            else:
                help(link.rest)
    help(link.rest)



def test_8_has_cycle():
    s = Link(1,Link(2,Link(3)))
    s.rest.rest.rest =s
    print(has_cycle(s))


# test_8_has_cycle()

    # def help_size(link,acc=0):
    #     if link == Link.empty:
    #         return acc
    #     else:
    #         return help_size(link.rest,acc+1)

def seq_in_link(link,sub_link):
    def help_find_first(link,value):
        new_link,is_find = None,False
        while not link == Link.empty:
            curr,rest = link.first,link.rest
            if curr == value:
                new_link = rest
                is_find = True
                break
            else:
                link = rest
        return (is_find,new_link)

    rs = True
    while not sub_link == Link.empty:
        is_find,new_link = help_find_first(link,sub_link.first)
        if is_find:
            link,sub_link = new_link, sub_link.rest
        else:
            rs = False
            break
    return rs










def test_seq_in_link():

    lnk1 = Link(53, Link(2, Link(3, Link(34))))
    lnk2 = Link(53, Link(3))

    print(seq_in_link(lnk1,lnk2))

# test_seq_in_link()


# 9 Iterators and Generators

def interator_demo():
    new_list =[2,3,6,8,8,3]
    # next(new_list)
    next(iter(new_list))
    g = iter(new_list)
    print(type(g))
    # g[1]
    a = [x for x in iter(new_list)]
    print(a)
    # b = len(g)
    # print(b)
# interator_demo()

def generate_constant(x):
    # """A generator function that repeats the same value x forever.
    # >>> area = generate_constant(51)
    # >>> next(area)
    # 51
    # >>> next(area)
    # 51
    # >>> sum([next(area) for _ in range(100)])
    # 5100
    # """
    while True:
        yield x

 # """A generator that yields items in SEQ until one of them matches TRAP, in which case that
 #    value should be repeatedly yielded forever.
 #    >>> trapped = black_hole([1, 2, 3], 2)
 #    >>> [next(trapped) for _ in range(6)]
 #    [1, 2, 2, 2, 2, 2]
 #    >>> list(black_hole(range(5), 7))
 #    [0, 1, 2, 3, 4]
 #    """

def black_hole(seq,trap):
    i,count =0,len(seq)
    while i<= count -1:
        temp = seq[i]
        if temp != trap:
            i = i+1
            yield temp
        else:
           yield from generate_constant(trap)

def test_black_hole():
    traped = black_hole([1,2,3],2)
    a =[next(traped) for _ in range(6)]
    print(a)

    b= list(black_hole(range(5), 7))
    print(b)

# test_black_hole()

def weird_gen(x):
    if x % 2 == 0:
        yield x*2

def test_weird_gen():
    wg = weird_gen(2)
    print(next(wg))
    print(next(weird_gen(2)))
    print(next(wg))

# test_weird_gen()

def greeter(x):
    while x % 2 !=0:
        print('hi')
        yield x
        print('bye')

def test_greeter():
    gen = greeter(5)
    print(type(gen))
    # print(next(gen))
    g = next(gen)
    g = (g,next(gen))
    print(g)
    print(next(gen))

# test_greeter()

def gen_inf(list):
    i,count = 0,len(list)
    while True:
        while i<= count-1:
            if i< count-1:
                yield list[i]
                i = i+1
            else:
                yield list [i]
                i =0

def test_gen_inf():
    t = gen_inf([3,4,5])
    a = [ next(t) for _ in range(9) ]
    print(a)

# test_gen_inf()


def naturals():
    i=1
    while True:
        yield i
        i =i+1

 # """
 #    >>> is_even = lambda x: x % 2 == 0
 #    >>> list(filter(range(5), is_even))
 #    [0, 2, 4]
 #    >>> all_odd = (2*y-1 for y in range (5))
 #    >>> list(filter(all_odd, is_even))
 #    []
 #    >>> s = filter(naturals(), is_even)
 #    >>> next(s)
 #    2
 #    >>> next(s)
 #    4
 #    """

def filter(iterable,fn):

    for i in iterable:
        if fn(i):
            yield i


def test_filter():
   for i in naturals():
       print(i)

# test_filter()
# """
#     >>> t = Tree(1, [Tree(2, [Tree(5)]), Tree(3, [Tree(4)])])
#     >>> print(list(tree_sequence(t)))
#     [1, 2, 5, 3, 4]
#     """

def tree_sequence(t):

    value = []
    def help(t):
        nonlocal value
        if Tree.is_leaf(t):
            value.append(t.label)
        else:
            curr,bs = t.label, t.branches
            value.append(curr)
            for branch in bs:
                help(branch)

    help(t)
    yield from value

def test_tree_sequence():
    t = Tree(1, [Tree(2, [Tree(5)]), Tree(3, [Tree(4)])])
    print(list(tree_sequence(t)))

# test_tree_sequence()


def make_digit_getter(n):
    def inner():
        rec = []
        def help():
            nonlocal n
            while n > 10:
                digit = n % 10
                rec.append(digit)
                n = n // 10
            rec.append(n)
            rec.append(sum(rec))
        help()
        yield from rec

    g = inner()
    def outer():
        return next(g)
    return outer


def test_make_digit_getter():
    year =8102
    get_year = make_digit_getter(year)
    for _ in range(4):
        print(get_year())

    print(get_year())

# test_make_digit_getter()


def iter(iterable):
    def iterator(msg):
        nonlocal iterable
        if msg == 'next':
            next = iterable[0]
            iterable = iterable[1:]
            return next
        elif msg == 'stop':
            raise StopIteration
    return iterator

def next(iterator):
    return iterator('next')

def stop(iterator):
    iterator('stop')

def test_last_one():
    lst =[1,2,3]
    iterator = iter(lst)
    elem = next(iterator)

    print(elem)
    print(next(iterator))


test_last_one()













