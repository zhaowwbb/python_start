print("Hello, VS Code!")
the_world = True
if the_world:
    print("The world is a wonderful place!") 
spam = 42
print(spam)
text = "The answer to the Ultimate Question of Life, The Universe, and Everything is " + str(spam)
# print(text)
# print(2 + 2)
# print(5**2)
# print(17 / 3)
print(17 // 3)
# print(17 % 3)
# # n
# # print
# tax = 12.5 / 100
# price = 100.50
# print(price * tax)
# print(price + price * tax)
# round(price * tax, 2)
# print("""\
#       des 
#       ssss
#       """)
# text    = ("The quick brown fox jumps over the lazy dog."
# "xxxx")
# print(text)
# the_world = "The world is a wonderful place!"
# print(the_world[0])
# print(the_world[7:12])
# print(len(the_world))
# squares = [1, 4, 9, 16, 25]
# squares.append(36)
# print(squares)
# print('id=' + str(id(squares)))

# def fib(n):
#     """Print a Fibonacci series up to n."""
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()
# fib(10)
# x = 10
# if x < 0:
#     print("Negative")
# elif x == 0:
#     print("Zero")
# else:
#     print("Positive")
# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))    

# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太': 'active'}
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]
# print(users)

# activeusers = {}
# for user, status in users.items():
#     if status == 'active':
#         activeusers[user] = status
# print(activeusers)
# for i in range(5):
#     print(i)
# print(list(range(5, 10)))   
# print(list(range(0, 10, 3)))

# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])  
# print(sum(range(4)))

# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         print(n, 'is a prime number')

# for num in range(2, 10):        
#     if num % 2 == 0:
#         print("Found an even number", num)
#         continue
#     print("Found a number", num)        
# # while True:
# #     pass    
# def initialize():
#     pass
# initialize()

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
        
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y} on the Y-axis")
        case Point(x=x, y=0):
            print(f"X={x} on the X-axis")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3      

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries -= 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)                          

# ask_ok('Do you really want to quit?') 

def power(x, y, / ,z=None):     
    if z is None:
        return x ** y
    else:
        return (x ** y) % z

power(2, 3  )   

def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)
print(f(5))

# fruits = ['apple', 'banana', 'cherry']
# for index, value in enumerate(fruits):
#     print(index, value) 

# print(fruits.count('apple'))
# fruits.append('pear')
# print(fruits.index('cherry'))
# fruits.reverse()
# print(fruits)
# fruits.sort()
# print(fruits)   
# fruits.pop()
# print(fruits)   

from collections import deque
queue = deque(["Eric", "John", "Michael"])  
queue.append("Terry")
queue.append("Graham")
print(queue.popleft())
print(queue.popleft())

squares = list(map(lambda x: x**2, range(10)))
print(squares)
from math import pi
print(list(map(lambda x: round(x, 2), [pi, pi*2, pi*3])))

a = [1, 2, 3, 4, 5]
del a[0]
print(a)
del a[1:3]
print(a)
t = 12345, 54321, 'hello!'
print(t[2])

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v) 