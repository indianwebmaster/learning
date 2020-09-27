'''
The Python lambda statement is an anonymous or unbound function and a pretty limited function at that.

While the examples below imply a lambda function returns a value, many time lambda functions are simply used to execute a procedure and not return anything.

You can pass multiple args to a lambda by separating with comma and no spaces
Lambda expressions must
- Use only expressions, not assignment statements
- Only use ONE expression, not multiple expressions
- Not declare and use local variables
'''
import math


def sqroot(x):
    return math.sqrt(x)

# Think of this as defining a function as f(x) = sqrt(x)
# & then determining f(64) - sqrt(64)
lam_sqroot = lambda x: math.sqrt(x)

print (sqroot(49))
print (lam_sqroot(64))

# Now obviously, assigning a lambda function to a variable is "identical" to a def <func_name>.
# This is not where the "power" of lambda shines. Instead, see its use in conjunction with
# the map() function (see learning/lambda_map for map() details)
numbers = [1,4,9,16]
result = map(lambda x: math.sqrt(x), numbers)
print (list(result))
# Above, the map function applies the lambda function over the iterable numbers

# Or do it all in one step
print(set(map(lambda x: math.sqrt(x), numbers)))

# Here is another way to do the same in one step, not using the map function. Less efficient, but demonstrates the use of "calling" a lambda function on declaration
print([(lambda x:math.sqrt(x))(y) for y in numbers])
# 'cause in this case, you can use conditionals in the one line loop as below
print([(lambda x:math.sqrt(x))(y) for y in numbers if y > 4])
# The above statement is equivalent to (without one line for and lambda)
def f_sqroot(x):
    return math.sqrt(x)

result=[]
for y in numbers:
    if y > 4:
        result.append(f_sqroot(y))
print(result)
