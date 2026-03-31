year = 2023
event = "Advent of Code"
print(f"Welcome to {event} {year}!")

yes_votes = 42
total_votes = 100
print(f"Voting results: {yes_votes / total_votes:.2%} yes votes")

s = "Hello, World!"
print(str(s))
print(repr(s))
str(1/7)  # str() produces a string that is nicely printable
print(str(1/7))
repr(1/7)  # repr() produces a string that is a valid Python expression 
print(repr(1/7)) 

x = 10 * 3.25
y = 200 * 200   
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
representations = repr((x, y, ('spam', 'eggs')))
print(representations)  

import math
print(f"The value of pi is approximately {math.pi:.3f}.")
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
for name, phone in table.items():
    print(f"{name:10} ==> {phone:10d}") 

animal = 'cow'
print(f"the {animal} says {repr(animal)}")
print(f"the {animal} says {animal!r}")  
print(f"the {animal} says {animal!s}")
print(f"the {animal} says {animal!a}")

bugs = 'roaches'
count = 1000    
area = 'living room'
print(f"There are {count} {bugs} in the {area}.")
print(f"Debugging {bugs=} {count=} {area=}.")    
print("We are the {} who say {}!".format('knights', 'Ni')  )
print("The story of {0}, {1}, and {other}.".format('Bill', 'Manfred', other='Georg'))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print("Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; "
      "Dcab: {0[Dcab]:d}".format(table))

table = {k: str(v) for k, v in vars().items()}
print(table)

for x in range(1, 11):
    print(f"{x:2} {x*x:3} {x*x*x:4}")
    print(repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4))      

'12'.zfill(5)  # zfill() pads a numeric string on the left with zeros to fill a field of the specified width
print('12'.zfill(5))
'-3.14'.zfill(7)
print('-3.14'.zfill(7))

import math
print('The value of pi is approximately %5.3f.' % math.pi)

f = open('workfile.txt', 'r')
for line in f:
    print(line, end='')  # end='' is used to avoid adding an extra newline character since lines already end with one   
# print(f.read())
f.close()   

import json
x = [1, 'simple', 'list']
print(json.dumps(x))  # json.dumps() converts a Python object into a JSON string    

# 10*(10/0)
# 4 + spam*3
# '2' + 2
try:
    x = int('N/A')
except ValueError:
    print("Could not convert data to an integer.")

class B(Exception):
    pass    
class C(B):
    pass
class D(C):
    pass    
for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")      

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly       
    x,y = inst.args
    print(f"x={x}, y={y}")  

import sys
try:
    f = open('workfile')
except OSError as err:
    print(f"OS error: {err}")   
except ValueError:
    print("Could not convert data to an integer.")  
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")   

# raise NameError('HiThere')

# try:
#     open('workfile', 'r')
# except OSError as err:
#     raise RuntimeError("Failed to open the file") from err
# finally :
#     print("This is executed last")

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")    
divide(2, 1)
divide(2, 0)

def f():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup('my exceptions', excs)
try:
    f()
except ExceptionGroup as eg:
    print(eg)   

# try:
#     raise TypeError('bad type')
# except Exception as e:
#     e.add_note('This is an additional note.')
#     e.add_note('This is another note.')
#     raise

def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()


scope_test()
print("In global scope:", spam)

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
x = Complex(3.0, -4.5)
print(x.real, x.imag)   

class Dog:
    kind = 'canine'         # class variable shared by all instances
    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
        self.tricks = []      # instance variable unique to each instance
    def add_trick(self, trick): 
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.kind, d.name, d.tricks)        # shared by all dogs
print(e.kind, e.name, e.tricks)        # shared by all dogs    

class Warehouse:
    purpose = 'storage'
    region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)

def f1(self, x, y):
    return min(x, x+y)
class C:
    f = f1
    def g(self):
        return 'hello world'
    h = g

class Base1:
    def __init__(self):
        print("Base1")
class Base2:
    def __init__(self):
        print("Base2")
class MultiDerived(Base1, Base2):
    def __init__(self):
        super().__init__()  # This will call Base1's __init__ due to MRO
        print("MultiDerived")   
d = MultiDerived()

from dataclasses import dataclass
@dataclass  
class employee:
    name: str
    id: int

e1 = employee('John Doe', 123)
print(e1)   

for element in [1, 2, 3]:
    print(element)  

s = 'abc'
it = iter(s)
print(next(it))






