# When you iterate over a list, you are "iterating" over the list. So, if a function returns a list - it returns a"iterables"
# def func_1():
#     alist=[]
#     for i in range(10):
#         alist.append(i)
#     return alist
#
# for x in func_1():
#     print (x)

# # On the other hand, if in the same function, you replace "return" with "yield", check out what you get
# # The function with the yield becomes a "generator" function, but with different result
# def func_2():
#     alist=[]
#     for i in range(10):
#         alist.append(i)
#         yield alist
#
# # This is because the generator function is "executed" every time in the loop below, versus above where it is executed ONCE, returns a list and we iterate over the list
# for x in func_2():
#     print (x)
#
# A proper generator function, which would simulate the same behaviour as the iterable function is below
def func_3():
    for i in range(10):
        yield(i)

# This is because the generator function is "executed" every time in the loop below, versus above where it is executed ONCE, returns a list and we iterate over the list
for x in func_3():
    print (x)
