import math
from lib import *
def make_counter():
    """Return a counter function.

    >>> c = make_counter()
    >>> c('a')
    1
    >>> c('a')
    2
    >>> c('b')
    1
    >>> c('a')
    3
    >>> c2 = make_counter()
    >>> c2('b')
    1
    >>> c2('b')
    2
    >>> c('b') + c2('b')
    5
    """
    count = {}
    def counter_inner(p,container = count):
        if container.__contains__(p):
            container[p].append(p)
        else:
            container[p]= [p]
        return len(container[p])
    return counter_inner


    return counter_inner

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self,item_name,unit_price):
        self.item_name = item_name
        self.unit_price = unit_price
        self.stock = 0
        self.amount = 0

    def restock(self,num):
        self.stock = self.stock + num
        return 'Current '+self.item_name+' stock: '+str(self.stock)

    def deposit(self,money):
        if not self.stock > 0:
            return 'Machine is out of stock. Here is your $'+str(money)+'.'
        else:
            self.amount = self.amount + money
            return 'Current balance: ' + '$' + str(self.amount)



    def vend(self):
        message=''
        if not self.stock >0:
            message= 'Machine is out of stock.'
        elif self.amount < self.unit_price:
            message = 'You must deposit $'+str(self.unit_price - self.amount)+' more.'
        elif self.amount >= self.unit_price:
            self.stock = self.stock - 1
            if self.amount > self.unit_price:
                message = f'Here is your {self.item_name} and ${self.amount - self.unit_price} change.'
            elif self.amount == self.unit_price:
                message = f'Here is your {self.item_name}.'
            self.amount = 0
        return message

def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(Tree(2, [Tree(4, [Tree(6)])]))
    [2, 4, 6]
    """
    rec = []
    def help(t):
        head, rest = t.label, t.branches
        rec.append(head)
        for branch in rest:
            help(branch)
    help(t)
    return rec



def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    """
    rec =[]
    def help(n):
        if n<10:
            rec.append(n)
        else:
            d,rest =n%10, n//10
            rec.append(d)
            help(rest)
    help(n)
    # rec.reverse()

    def help2(arr):
        if len(arr) ==1:
            return Link(arr[0])
        else:
            item = arr.pop()
            return Link(item,help2(arr))
    return help2(rec)


def generate_paths(t, x):
    """Yields all possible paths from the root of t to a node with the label x
    as a list.
    # >>> sorted(list(path_to_2))

    >>> t1 = Tree(1, [Tree(2, [Tree(3), Tree(4, [Tree(6)]), Tree(5)]), Tree(5)])
    >>> print(t1)
    1
      2
        3
        4
          6
        5
      5
    >>> next(generate_paths(t1, 6))
    [1, 2, 4, 6]
    >>> path_to_5 = generate_paths(t1, 5)
    >>> next(path_to_5)
    [[1, 2, 5], [1, 5]]

    >>> t2 = Tree(0, [Tree(2, [t1])])
    >>> print(t2)
    0
      2
        1
          2
            3
            4
              6
            5
          5
    >>> path_to_2 = generate_paths(t2, 2)

    >>>
    [[0, 2], [0, 2, 1, 2]]
    """
    rec = []

    def help(tt, nd, acc):
        curr, rest = tt.label, tt.branches
        acc.append(curr)
        if curr == nd:
            rec.append(acc)
        for branch in rest:
            temp = acc[:]
            help(branch, nd, temp)

    help(t, x, [])
    yield rec

class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.current_year.

    >>> mint = Mint()
    >>> mint.year
    2019
    >>> dime = mint.create(Dime)
    >>> dime.year
    2019
    >>> Mint.current_year = 2100  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2019
    >>> nickel.worth()  # 5 cents + (81 - 50 years)
    36
    >>> mint.update()   # The mint's year is updated to 2100
    >>> Mint.current_year = 2175     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (156 - 50 years)
    116
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (156 - 50 years)
    126

    """
    current_year = 2019

    def __init__(self):
        self.update()

    def create(self, kind):
        return kind(self.year)

    def update(self):
        Mint.year = Mint.current_year

class Coin:
    def __init__(self, year):
        self.year = year

    def worth(self):
        over_fifty = Mint.current_year - self.year
        if over_fifty > 50:
            return self.cents + (over_fifty -50)
        return self.cents

class Nickel(Coin):
    cents = 5

class Dime(Coin):
    cents = 10


def remove_all(link , value):
    """Remove all the nodes containing value in link. Assume that the
    first element is never removed.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    """
    rs = Link(link.first)
    curr_p = rs

    def help(link, item):
        nonlocal curr_p
        curr, rest = link.first, link.rest
        if rest == Link.empty:
            if not curr == item:
                curr_p.rest = Link(curr)
        else:
            if curr == item:
                help(rest, item)
            else:
                curr_p.rest = Link(curr)
                curr_p = curr_p.rest
                help(rest, item)

    help(link.rest, value)
    return rs


def deep_map(f, link):
    """Return a Link with the same structure as link but with fn mapped over
    its elements. If an element is an instance of a linked list, recursively
    apply f inside that linked list as well.

    >>> s = Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> print(deep_map(lambda x: x * x, s))
    <1 <4 9> 16>
    >>> print(s) # unchanged
    <1 <2 3> 4>
    >>> print(deep_map(lambda x: 2 * x, Link(s, Link(Link(Link(5))))))
    <<2 <4 6> 8> <<10>>>
    """
