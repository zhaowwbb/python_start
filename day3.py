import os
import smtplib
os.getcwd() 
# with open('day2.txt') as f:
#     print(f.read())
# dir(os)
# help(os)

import shutil
# shutil.copyfile('day2.txt', 'day3.txt')  # copies contents of 'day2.txt' to 'day3.txt'
# shutil.copy('day2.txt', 'day3.txt')  # copies 'day2.txt' to 'day3.txt' (also copies permissions)
# shutil.copytree('dir1', 'dir2')  # recursively copy an entire directory   

import glob
print(glob.glob('*.py'))  # lists all .txt files in the current directory

import sys
print(sys.argv)  # prints the list of command-line arguments passed to the script

import argparse
parser = argparse.ArgumentParser(description='Process some integers.')  
parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum,
                    default=max, help='sum the integers (default: find the max)')
# args = parser.parse_args()
# print(args.accumulate(args.integers))
# print(args.accumulate(args.))    

sys.stderr.write('Warning, log file not found starting a new one\n')    

import re
r1 = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')  # finds all words starting with 'f'
r2 = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')  # replaces repeated words with a single instance 
print(r1)
print(r2)

import math
print(math.cos(math.pi / 4))  # cosine of 45 degrees    
print(math.log(1024, 2))  # logarithm base 2 of 1024

import random
print(random.choice(['apple', 'pear', 'banana']))  # randomly selects an element from the list
print(random.sample(range(100), 10))  # randomly selects 10 unique numbers from
print(random.random())  # generates a random float in the range [0.0, 1.0)
print(random.randrange(6))  # randomly selects an integer from the range [0,    6)          

import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.25, 1.25, 3.25]
print(statistics.mean(data))  # calculates the mean of the data
print(statistics.median(data))  # calculates the median of the data
print(statistics.variance(data))  # calculates the variance of the data 

# import urllib.request
# import gzip
# import io
# with urllib.request.urlopen('http://www.python.org/') as response:
#     raw_data = response.read()  # reads the raw bytes from the response
#     if response.info().get('Content-Type') == 'gzip':
#         html_bytes = gzip.decompress(raw_data)  # decompresses the gzip content
#         html = html_bytes.decode('utf-8')  # decodes the bytes to a string
#     else:
#         html_bytes = gzip.decompress(raw_data) 
#         html = html_bytes.decode('utf-8')  # decodes the bytes to a string    
#         print(html)

# import smtplib
# server = smtplib.SMTP('localhost')
# server.sendmail('aaa@test.com', 'bbb@test.ca', 'Subject: Hello\n\nThis is the body of the email.')
# server.quit()  # closes the connection to the SMTP server   

import datetime as dt
now = dt.datetime.now()  # gets the current date and time   
print(now)  # prints the current date and time
print(now.year, now.month, now.day)  # prints the year, month, and day of the current date
print(now.strftime("%m-%d-%Y %H:%M"))  # formats the date and time as a string  
birthday = dt.datetime(1990, 5, 17)  # creates a datetime object for a specific date
print(birthday)  # prints the birthday datetime object
age = now - birthday  # calculates the age by subtracting the birthday from the current date
print(age.days)  # prints the age in days

import zlib
s = b'For the past several years, I have specialized in building scalable, cloud-native platforms where I leverage PostgreSQL for complex data modeling, and Kafka or Redis for event-driven interoperability. I have a strong background in Python and Java, and I am passionate about designing and implementing robust, efficient, and maintainable software solutions. I am always eager to learn new technologies and best practices to stay at the forefront of the industry.'  # a byte string
print('len(s)=',len(s))  # prints the length of the byte string
t = zlib.compress(s)  # compresses the byte string
print('len(t)=',len(t))  # prints the length of the compressed byte string
# print(zlib.compress(s))  # compresses the byte string   
# print(zlib.decompress(zlib.compress(s)))  # decompresses the compressed byte string
# print(zlib.crc32(s))  # calculates the CRC-32 checksum of the byte

from timeit import Timer
t = Timer('for i in range(10): oct(i)').timeit()  # measures the execution time of the code snippet
print(t)  # prints the execution time

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)  # calculates the average by dividing the sum by the number of values              

import doctest
print(doctest.testmod())  # runs the doctest on the average function and prints the results     

# import unittest 
# class TestAverage(unittest.TestCase):
#     def test_average(self):
#         self.assertEqual(average([20, 30, 70]), 40.0)  # tests that the average function returns the expected result    
#     def test_round(self):    
#         self.assertEqual(round(average([1, 2, 3, 4, 5]), 3), 3.0)  # tests another case for the average function
# if __name__ == '__main__':
#     unittest.main()  # runs the unit tests when the script is executed directly 

import reprlib
print('reprlib=',reprlib.repr(set('supercalifragilisticexpialidocious')))  # provides a shortened string representation of the set of characters in the word   

import pprint
t = [[[['black', 'cyan', 'blue', 'yellow', 'white'],
       ['red', 'maroon', 'yellow', 'olive', 'lime'],
       ['fuchsia', 'purple', 'green', 'navy', 'teal']]]]    
print('pprint=',pprint.pprint(t, width=30))  # pretty-prints the nested list with a specified width

import textwrap
doc = """The wrap() method is just like fill() except that it returns a list of strings instead of one big string with newlines to separate the wrapped lines."""
print('textwrap=',textwrap.fill(doc, width=40))  # wraps the text to a specified width and returns it as a single string with newlines      

import locale
print('locale=',locale.setlocale(locale.LC_ALL, ''))  # sets the locale to the user's default setting (usually specified in the environment) and prints the current locale setting  
conv = locale.localeconv()  # gets the locale conventions for formatting numbers
print('localeconv=',conv)  # prints the locale conventions, which include information about decimal point, thousands separator, and currency symbol
locale.format_string("%d", 1234567, grouping=True)  # formats the number with grouping (e.g., adding commas as thousands separators)
print(locale.format_string("%d", 1234567, grouping=True))  # prints the formatted number with grouping according to the current locale settings 
print(locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], 1234567.8), grouping=True))  # formats the number as currency according to the current locale settings, including the currency symbol and appropriate decimal places        

from string import Template
t = Template('The ${color} in the ${thing} falls mainly in the ${place}.')  # creates a template string with placeholders for color, thing, and place
print('Template=',t.substitute(color='rainbow', thing='sky', place='mountains'))  # substitutes the placeholders in the template with the provided values and prints the resulting string   

import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
# for name in photofiles:   
class BatchRename:
    delimiter = '%'
# fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
    fmt = 'Ashley_%d-date %n-seqnum %f-format'  # example format string for renaming files
t = Template('Ashley_${d}-date ${n}-seqnum ${f}-format')
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))
# print(fmt.format(name='Guido', n=37))  # formats the string using named     
# 

import struct
print(struct.pack('>I', 10240099))  # packs the integer 10240099 into a bytes object using big-endian format
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x00'))  # unpacks the bytes object into a tuple of values according to the specified format (big-endian unsigned int followed by big-endian unsigned short)   

with open('day3.bin', 'wb') as f:
    f.write(struct.pack('>I', 10240099))  # writes the packed integer to a binary file  

import threading,zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile
    def run(self):
        with zipfile.ZipFile(self.outfile, 'w') as zf:
            zf.write(self.infile)    

background = AsyncZip('workfile.txt', 'day2.zip')  # creates an instance of the AsyncZip class to zip the file 'day2.txt' into 'day2.zip'
background.start()  # starts the background thread to perform the zipping operation     

print('The main program continues to run in foreground.')  # prints a message indicating that the main program is still running while the background thread is performing its task
background.join()  # waits for the background thread to finish before proceeding    
print('Main program waited until background thread was done.')  # prints a message indicating that the main program has waited for the background thread to complete its task   

import logging
logging.debug('Debugging information')  # logs a debug message
logging.info('Informational message')  # logs an informational message
logging.warning('Warning:config file %s not found', 'server.conf')  # logs a warning message with formatted string
logging.error('Error occurred')  # logs an error message
logging.critical('Critical error -- shutting down')  # logs a critical error message

import weakref, gc
class A:
    def __init__(self, value):
        self.value = value  
    def __repr__(self):
        return f"A({self.value})"  # provides a string representation of the object for debugging purposes  

a = A(10)  # creates an instance of class A with a value of 10
d = weakref.WeakValueDictionary()  # creates a weak reference dictionary to hold weak references to objects
d['primary'] = a  # adds a weak reference to the object 'a' in the dictionary with the key 'primary'            
print(d['primary'])  # prints the object referenced by the key 'primary' in the dictionary (should print A(10))
del a  # deletes the strong reference to the object 'a'
gc.collect()  # forces garbage collection to clean up any unreferenced objects      

from array import array
a = array('H', [4000, 10, 700, 22222])  # creates an array of unsigned short integers with the specified values
print(a)  # prints the array object
sum(a)  # calculates the sum of the elements in the array
print(sum(a))  # prints the sum of the elements in the array
a[1:3]  # slices the array to get a subset of its elements
print(a[1:3])  # prints the sliced portion of the array (should print array('H', [10, 700]))    

from collections import deque
d = deque(['task1', 'task2', 'task3'])  # creates a deque (double-ended queue) with the specified tasks
d.append('task4')  # adds 'task4' to the right end of the deque
print(d)  # prints the contents of the deque (should print deque(['task1', 'task2', 'task3', 'task4']))
d.appendleft('task0')  # adds 'task0' to the left end of the deque
print(d)  # prints the contents of the deque (should print deque(['task0',  'task1', 'task2', 'task3', 'task4']))
d.pop()  # removes and returns the rightmost element of the deque (should return 'task4')
print(d)  # prints the contents of the deque after popping (should print deque(['task0', 'task1', 'task2', 'task3']))
d.popleft()  # removes and returns the leftmost element of the deque (should return 'task0')
print(d)  # prints the contents of the deque after popping from the left (should print deque(['task1', 'task2', 'task3']))  

import bisect
scores = [100, 90, 80, 70, 60]  # a list of scores in descending order
bisect.bisect(scores, 85)  # finds the insertion point for 85   
print('(scores, 85)=',bisect.bisect(scores, 85))  # prints the insertion point for 85 (should print 2, since 85 would be inserted between 90 and 80)
bisect.insort(scores, 85)  # inserts 85 into the list while maintaining sorted order
print(scores)  # prints the list of scores after inserting 85 (should print [100, 90, 85, 80, 70, 60])

from heapq import heapify, heappush, heappop
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]  # a list of unsorted numbers
heapify(data)  # transforms the list into a heap in-place       
print(data)  # prints the heapified list (the smallest element will be at the root of the heap)
heappush(data, -5)  # pushes the value -5 onto the heap, maintaining the heap property
print(data)  # prints the heap after pushing -5 (should show -5 as the new smallest element)
heappop(data)  # pops and returns the smallest element from the heap (should return -5)     
print(data)  # prints the heap after popping the smallest element (should no longer contain -5)

from decimal import *
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))  # performs decimal arithmetic to avoid floating-point precision issues (should print 0)
getcontext().prec = 36  # sets the precision for decimal arithmetic to 36 places    
print(Decimal(1) / Decimal(7))  # performs decimal division with the specified precision (should print a decimal representation of 1/7 with 36 digits of precision)
round(Decimal('1.23'), 1)  # rounds the decimal number to 1 decimal place (should return Decimal('1.2'))
print(round(Decimal('1.23'), 1))  # prints the rounded decimal number   
round(Decimal('0.70')*Decimal('1.25'), 2)  # rounds the result of multiplying 0.70 by 1.00 to 2 decimal places (should return Decimal('0.70'))  
print(round(Decimal('0.70')*Decimal('1.25'), 2))  # prints the rounded result of the multiplication (should print 0.70)








