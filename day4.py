import sys
print(sys.version)
print(sys.path)

x = 3.14159
print(x)    
print(x.as_integer_ratio())
print(x.is_integer())
# print(x.is_nan())   
# print(x.is_infinite())

q, r = divmod(10, 3)
print(q, r) 
print('format(0.1, ".25f")=', format(0.1, '.25f'))

from decimal import Decimal
x = Decimal('0.1')
print(x)
Fraction = __import__('fractions').Fraction
f = Fraction.from_float(0.1)
print(f)
print(f.as_integer_ratio())
# f.as_integer_ratio()
Decimal.from_float(0.1)
print(Decimal.from_float(0.1))

import os
filename = os.environ.get('FILENAME', 'default.txt')
if filename and os.path.exists(filename):
    print(f"File '{filename}' exists.")
else:    print(f"File '{filename}' does not exist.")

import site
print(site.getsitepackages())

import _asyncio
_asyncio
print(_asyncio.__file__)


