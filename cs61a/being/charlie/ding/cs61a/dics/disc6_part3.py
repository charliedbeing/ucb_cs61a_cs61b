class Pet:
    def __init__(self,name,owner):
        self.isLive = True
        self.name = name
        self.owner = owner

    def eat(self,thing):
        print(self.name + " ate a " + str(thing) +" ! ")

    def talk(self,content):
        print(self.name + content )

class Dog(Pet):
    def talk(self):
        print("I am a dog ", "Wang,Wang")

class Cat(Pet):

    def __init__(self,name,owner,lives=9):
        self.name = name
        self.owner = owner
        self.lives = lives
        self.isLive = self.lives > 0

    def lost_one(self):
        self.lives = self.lives-1
        self.isLive = self.lives > 0

    def __str__(self):
        if(self.isLive):
            return 'my name is ' + self.name + ' I have lives is ' + str(self.lives)
        else:
            return '....'

    def eat(self,thing):
        if self.isLive:
            super().eat(thing)
        else:
            print('!!!!')




def test_inheriant():
    dog = Dog('lili','Charlie')
    dog.talk()
    dog.eat('da gu tou')

    print(dog.isLive)

    cat = Cat('mimi','Fiona')
    # print(cat.isLive)

    cat.lost_one()
    cat.lost_one()

    for _ in range(1,10):
        cat.lost_one()


    print(cat)

    cat.eat('niu gu tou !!')


# test_inheriant()

class Foo:
    bar=0
    def __init__(self,num):
        Foo.bar = num
        self.bar = Foo.bar
        self.__key='d1e2f9A!@'

    def g(self,num):
        return num + self.bar

def test_foo():
    x = Foo(1)
    print(x.g(3))
    print(x.g(5))
    x.bar = 5
    print(x.g(5))
    # print(x.__key)
    # print(x._Foo__key)


test_foo()



