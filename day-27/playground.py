
#unlimited positional arguments
# def add(*args):
#     print(args[-1])
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
#
# print(add(3,5,7,5,6,7,95,45,35,))

def calculate(n,**kwargs):
    print(kwargs)
    n +=kwargs["add"]
    n *=kwargs["multiple"]
    return n


print(calculate(2,add= 3,multiple = 5))

class Car:
    def __init__(self,**kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my = Car(make="subraeu")
print(my.make)