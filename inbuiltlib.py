#math module
import math
x=10.8 
print(math.ceil(x))
print(math.floor(x))
print(math.trunc(x))

x=3
print(math.exp(x))
print(math.log10(x))
print('-'*45)

x=90
print(math.sin(x))
print(math.cos(x))
print(math.tan(x))
print('-'*45)

print(math.pi)
print(math.e)
print('-'*45)
#random module

import random

random.seed(40)
print (random.random())
print(random.randint(1,11))
print(random.choice([1,2,3,4,5]))
print(random.sample([1,2,3,4,5],2))
print(random.uniform(1.0,3.0))
print('-'*45)
#date-time
import datetime
print(datetime.datetime.now())

print(datetime.datetime.now().strftime("%m/ %d /%y  %H:%M:%S"))

print('-'*45)

#collections
from collections import Counter,defaultdict
lst=[1,2,3,4,5,5,5,6,6,7]
print(Counter(lst))
print('-'*45)

d=defaultdict(int)
d['a']+=2
print(d)
print('-'*45)
'''
d=OrderedDict()
d['one']=1
d['two']=2
print(d)
print('-'*45)'''
#strings
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print('-'*45)

print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print('-'*45)

print(string.punctuation)



















