#python2
"""
In C++, the only low level array structure available is a fixed array
    int my_cplus_array[16];
    This statement defines a variable my_cplus_array as an array, with a size of 16 elements
"""

"""
In python, the "only" array structure available is the dynamic list[]/ So,
"""
#LEARN_1 my_py_array = []
"""
This statement defines a variable my_py_array with no size - so theoretically unlimited.

However, the py variable is not an "array" in the true sense - because the definition of an array
is that an "insert" operation is an Order(1) operation for any valid position in the array.
This is true for the C++ case
    my_cplus_array[2] = 101;

However, if you try to perform the operation in python
"""
#LEARN_1 my_py_array[2] = 101
"""
You will see that it fails. Lets go ahead and comment the line above .....

In order for this work, you have to perform the operation as below
"""
#LEARN_2 my_py_array = []
#LEARN_2 my_py_array.append(101)
"""
So, what you are doing here, is not really an array operation - because append implies "extending the
size", and an array by "definition" is of fixed size.

So, how do you define a true "array" in python using the list[] primitive. See below
"""
#LEARN_3 my_py_array_2 = [] * 16
"""
That seems right ... we are defining an array and allocating 16 entries to it.
Let's test this.
"""
#LEARN_3 my_py_array_2[2] = 101
"""
Well, it still fails. Why did that happen. It is because what we are really doing is we are allocating 16 "empty" list
 items and each list item would need to be "extended" to be able to add anything. Not what we wanted ....

So, lets try a different way
"""
#LEARN_4 my_py_array_3 = [None] * 16
#LEARN_4 my_py_array_3[1] = 101
"""
This works. Can you explain why?
"""

"""
Conclusion
So, in conclusion, in python, if you have to define an "array", you need to follow the requirements of an array in
that the size of the array needs to be known at the time of creation. Yes, a "python" array can be extended ....
but that is just because we are using a more powerful primitive (list) to create the array - but that is outside
of the "true" definition is an array.

Once defined as an array, my_py_array_3 will provide the Order(1) expense for a get(index) or set(index,value) operation
"""