'''
The map() function applies a given function to each item of an iterable (list, tuple etc.) and returns a list of the results.
The syntax of map() is:
    map(function, iterable, ...)
        function - map() passes each item of the iterable to this function
        iterable - iterable which is to be mapped (see learning/yield_iterables_generators for iterables

        The returned value from map() (the map object) can be converted using functions like list() or set()
'''
import math


def sqrt(x):
    return math.sqrt(x)

# See learning/lambda_map for lambda
lamb_sqrt = lambda x: math.sqrt(x)

numbers = [1,4,9,16]

# Use map in conjunction with a regular function
result = map(sqrt, numbers)
# print (result)
# print (list(result))

# Use map in conjunction with a 'named' lambda function
result = map(lamb_sqrt, numbers)
# print (result)
# print (list(result))

# A very common use, use map in conjunction with a lambda definition in the statement
result = map(lambda x: math.sqrt(x), numbers)
print (result)
print (list(result))

# Or do it all in one step plus use set() or list()
print(set(map(lambda x: math.sqrt(x), numbers)))
print(list(map(lambda x: math.sqrt(x), numbers)))

# You would think a single line for loop could also be used instead of map
# [process-using-thing for thing in many_things]
print([lambda x: math.sqrt(x) for y in numbers])
# But, as you can see, this just creates multiple lambda functions. Not useful.
# So, you change it like this ... where you execute each function by passing "y")
print([(lambda x: math.sqrt(x))(y) for y in numbers])
# It is not as efficient as map, as you will create the same lambda function at each iteration & execute it in this case

