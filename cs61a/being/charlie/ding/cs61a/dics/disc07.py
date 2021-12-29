from lib import *

a = Link(1,Link(2,Link(3,Link(4,Link(5)))))

print(len(a))

print(a.__getitem__(4))
