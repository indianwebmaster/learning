'''
We talked about map() function in learn_map_1.py. filter() and reduce() are "parallel" functions to map() with their own differences

filter(function, iterables): Processes iterables through function but only returns elements where function result is True
reduce(function, iterables): Unlike map() and filter(), reduce returns a single value. It takes the result of each iterable through function and uses it as 1st arg the next time

reduce() requires an import (from functools import reduce)
'''

def square_numbers(x):
    return (x*x)

numbers = range(1,5)
print(set(map(square_numbers, numbers)))
# -----------------------
def check_number(x):
    return (x >= 0)

print(set(filter(check_number, range(-5,5))))
# -----------------------
from functools import reduce
def mult_numbers(x,y):
    return (x*y)
print(reduce(mult_numbers,numbers))
# -----------------------
# Same operations above using lambda
print(set(map(lambda x: x*x, numbers)))

print(set(filter(lambda x: x>= 0, range(-5,5))))

print(reduce(lambda x,y:x*y, numbers))