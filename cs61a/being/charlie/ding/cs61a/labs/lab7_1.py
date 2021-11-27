
def naturals():
    i = 1
    while True:
        yield i
        i += 1


def scale(it, multiplier):
    new_generator= iter([])
    if type(it) == type([]):
        yield from [x*multiplier for x in it]
    elif type(it) == type(naturals()):
        new_generator = naturals()
        while True:
            temp = next(new_generator)
            yield temp* multiplier

m = scale(naturals(), 2)
t = [next(m) for _ in range(5)]

# print(t)

# print(type(naturals()))

def hailstone(n):
    if n==1:
        print(n)
    elif n%2 ==0:
        print(n)
        return hailstone(n//2)

    else:
        print(n)
        return hailstone(n*3 +1)
#
# hailstone(10)

def hailstone2(n):
    rec =[]
    def help(n,acc):
        if n == 1:
            acc.append(1)
        elif n % 2 == 0:
            acc.append(n)
            return help(n // 2,acc)

        else:
            acc.append(n)
            return help(n * 3 + 1,acc)
    help(n,rec)

    yield from rec


class Car(object):
    num_wheels =4
    gas =30
    headlight =2
    size='Tiny'

    def __init__(self,make,model):
        self.make =make
        self.model = model
        self.color = 'Not color yet'
        self.wheels = Car.num_wheels
        self.gas = Car.gas

    def paint(self,color):
        self.color = color
        return self.make + ' ' + self.model + ' is now '+ self.color

    def drive(self):
        if self.wheels < Car.num_wheels or self.gas <0:
            return 'Cannot drive'
        self.gas -= 10
        return self.make + ' ' + self.model + ' goes vroom'

    def pop_tire(self):
        if self.wheels>0:
            self.wheels -=1

    def fill_gas(self):
        self.gas += 20
        return 'Gas level' + str(self.gas)

class MonsterTruck(Car):
    size = 'Monster'

    def rev(self):
        print('Vroom! This Monster Truck is huge!')

    def drive(self):
        self.rev()
        return Car.drive(self)


charlie_dream_car = Car('Tesla','Model SSS')


def present_in_object():
    for item in charlie_dream_car.__dict__:
        print(item)
    charlie_monster = MonsterTruck('Tesla', 'Model SSSXXXX')
    for item2 in charlie_monster.__dir__():
        print(item2)

def present_car_basic_1():
    charlie_car_1 = Car('Jetta','LX')
    charlie_car_1.gas =100

    charlie_car_1.drive()

    print(charlie_car_1.gas)
    charlie_car_1.drive()
    print(charlie_car_1.gas)
    print(Car.gas)
    charlie_car_1.fill_gas()
    print(charlie_car_1.gas)


def present_car_basic_2():
    car_2= Car('Civic','Ex')
    car_2.wheels =2

    # print(car_2.drive())
    # print(Car.drive())
    car_2.wheels =4
    # print(Car.drive(car_2))

    car_3 = MonsterTruck("Ford", 'FX150')

    print(Car.drive(car_3))

    print("----")

    print(car_3.drive())

    print(car_3.drive(car_2)) #drive() takes 1 positional argument but 2 were given
    print("----")
    print(MonsterTruck.drive(car_3))

   # print(Car.rev(car_3))  # type object 'Car' has no attribute 'rev'

present_car_basic_2()


