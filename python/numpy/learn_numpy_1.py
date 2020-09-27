'''
    Numpy is a math library for python. It enables us to do computation efficiently, effectively and has amazing capabilities

    In numpy, array, matrix and vector and used interchangeably

    For multi-dimensional arrays, you specify as (num_rows, num_columns)


'''
import numpy as np
import random

# There is no difference between a simple list and numpy array at first glance
# Print of numpy array just shows separated by spaces, instead of commas
def func_01():
    # list
    plist = [1,2,3,4,5,6]
    #numpy array
    nplist = np.array([1,2,3,4,5,6])

    print(plist)
    print (nplist)

# Some simple numpy creation/arrange functions
# arange(from_incl, upto_excl, [step])
# shape() - returns (num_rows,num_cols) - see below for result for nplist and why?
# reshape() - transpose or convert to multidimension matrix
# zeros(tuple(nrows,ncols)) - create a matrix filled with (float) 0
# eye(n) - create an n x n Identity matrix (diagonals filled with 1. )
# random.rand()
def func_02():
    # list
    plist = [1,2,3,4,5,6]
    # numpy array
    nplist = np.array([1,2,3,4,5,6])

    print ('np.arange')
    print(np.arange(10, 20))
    print (np.arange(10, 20, 2))
    print(np.arange(20, 10, -2))

    print('np.shape')
    print (nplist.shape)
    # Instead see what you get when you make some changes
    nplist2 = np.array([[1, 2, 3, 4, 5,6]])
    print(nplist2.shape)
    # This results looks better in the "num_rows,num_cols" format that we expected.
    # Well, that because in the first case, it is really saying 9 rows with 1 column each

    print('np.reshape')
    print(nplist.reshape(1,6))  # See interesting result for this. Makes it == nplist2
    print(nplist2.reshape(6,1))
    print(nplist2.reshape(6,))  # See interesting result for this. Makes it == nplist, but different from previous (5,1)
    print(nplist2.reshape(3, 2))
    print(nplist2.reshape(2, 3))

    print('np.zeros')
    print(  np.zeros(6)  )
    print(  np.zeros(6,)  ) # same as above
    print(  np.zeros((6)) ) # same as above
    print(  np.zeros((6,))) # same as above

    print(  np.zeros((3, 2)) )
    print(  np.zeros((2, 3)) )

    print('np.eye')
    print(np.eye(6))    # Create a 6x6 identity matrix

    print('np.random.rand')
    print(np.random.rand(2, 3))
    print(np.random.rand(2))    # 1 row with two entries
    print(np.random.rand(2,))   # Same as previous
    print(np.random.rand(1,2))  # Not the same as previous two, 1 row with 1 list with 2 elements
    print(np.random.rand(2,1))

    print('np.random.randint')
    print(np.random.randint(low=10,high=50,size=6))
    print(np.random.randint(10, 50, 6))    # same as previous

    print('Random without dups - 3 step process')
    nums = np.arange(10,50)
    np.random.shuffle(nums)
    print(np.array(nums[:6]))
    print('Random without dups - non-numpy process - needs import random')
    print(np.array(random.sample(range(10,50), 6)))

    print('Randomize a fixed set of numbers or characters')
    possible_options = ['ab','bc','cd','de','ef']
    print (np.random.choice(possible_options,20))

# Next, here are some matrix arithmetic operations
def func_03():
    # Two ways to create a list with some known values
    print ("Data")
    nplist1=np.arange(10,16).reshape(2,3)
    nplist2 = np.array(range(20,26)).reshape(3, 2)
    print(nplist1)
    print(nplist2)

    i=0
    i += 1; print (i, nplist1 + nplist1)       # This is adding the values of two "like" matrices
    i += 1; print (i, nplist1 * nplist1)       # This is multiplying the values of two "like" matrices
    i += 1; print (i, np.dot(nplist1, nplist2))    # ( (2x3) * (3x2) = (2x2) ) This is matrix multiplication, diff than the previous one.

    i += 1; print(i, np.sum(nplist1))   # Sum all elements in matrix
    i += 1; print(i, np.sum(nplist1,axis=1))  # Sum all row elements in matrix
    i += 1; print(i, np.sum(nplist1, axis=0))  # Sum all column elements in matrix

    i += 1; print(i, np.diff(nplist1))   # Diff between adjacent elements in matrix. Result for (2x3) is (2x2)
    i += 1; print(i, np.diff(nplist2))  # Diff between adjacent elements in matrix. Result for (3x2) is (3x1)
    i += 1; print(i, np.diff(nplist1,n=2))   # Repeat diff operation 2 times. Result for (2x3) is (2x1)

    i += 1; print(i, nplist1 + 300)   # Add 300 to EACH element of array
    i += 1; print(i, nplist2 + 300)   # Add 300 to EACH element of array
    i += 1; print(i, nplist1 * 300)   # Multiply 300 to EACH element of array

    i += 1; print(i, nplist1 == nplist1)   # Compare two mxn matrices, returns a mxn matrix with True/False
    i += 1; print(i, nplist1, nplist1[nplist1 > 12]) # Find all values greater than 12

    list1=[1,0,2,0]
    i += 1; print(i, list1, np.nonzero(list1))  # Find indices of nonzero elements



# Some add/delete operations
def func_04():
    print ("Data")
    nplist1=np.arange(10,16)
    nplist2=np.arange(20,26).reshape(3, 2)
    print(nplist1)
    print(nplist2)

    i = 0
    # Append one element
    i += 1; print (i, np.append(nplist1,101))
    i += 1; print (i, np.append(nplist1,[101])) # Same as previous
    print (nplist1) # Capture the return of np.append() if you want to do inplace replacement.
    i += 1; print(i, np.append(nplist2, 101))   # Converts or flattens the multidimen array

    # Append another list
    i += 1; print(i, np.append(nplist2, [101,102]))   # Converts or flattens the multidimen array

    # Create a 2x3 matrix merging two 1x3 matrices (row stack or vstack)
    nplist11 = np.arange(10,13)
    nplist12 = np.arange(20, 23)
    i += 1; print(i, np.vstack(  (nplist11, nplist12)  )    )

    # Create a 3x2 matrix merging two 1x3 matrices (column stack)
    i += 1; print(i, np.column_stack(  (nplist11, nplist12)  )    )

    # Extract some elements or rows
    i += 1; print (i, nplist1[1:3])     # (from_incl, to_excl). Easy to see for a 1 dimen array
    i += 1; print (i, nplist2[1:3])     # In this case, you get "two rows from a 3x2 matrix", not 2 elements
    i += 1; print (i, nplist1[:-1])     # All except last element
    i += 1; print (i, nplist1[-1:])     # ONLY last element
    i += 1; print (i, nplist2[:-1])     # All except last row
    i += 1; print (i, nplist2[-1:])     # ONLY last row

# These are somewhat "advanced", but useful operations
def func_05():
    # You have two arrays, which are related to each other.
    # You want to sort one array, but retain the association with the other array
    nplist1 = np.array(random.sample(range(10,50),10))      # array without dups
    nplist2 = np.array(random.sample(range(10, 50), 10))    # array without dups
    print(nplist1)
    print(nplist2)
    sorter = np.argsort(nplist1)
    print(nplist1[sorter])
    print(nplist2[sorter])
    # --------------------------------------------------------------------------
    # You have one array with values, and another array with index positions
    # You want to list the array in the order of the index positions in the other array
    nplist3 = np.array(list('0123456789'))
    index_positions_list = np.random.randint(0,10,10)

    print (nplist3)
    print (index_positions_list)
    # Here's the trick
    print (nplist3[index_positions_list])
    # --------------------------------------------------------------------------
    # You have one array with values
    # You want to find how many values are present smaller than each value
    nplist4 = np.random.randint(0, 10, 10)
    print(nplist4)
    print(np.argsort(np.argsort(nplist4)))  # ONLY WORKS WELL FOR NON-DUP LIST
    # --------------------------------------------------------------------------
    # You have one array with string values, many duplicates
    # You want to convert this to list of numbers, with each string a uniq number and dups with same number
    nplist5 = np.random.choice(['a','b','c','d','e','f','g','h'],10)
    uniq_list, counts_list = np.unique(nplist5, return_inverse=True)
    print(nplist5)      # Original List
    print(uniq_list)    # Uniq list
    print(counts_list)  # Position list
    # You want to convert the list of numbers back to string values
    print(uniq_list[counts_list])   # Should be same as Original List
    # --------------------------------------------------------------------------
    # You have two lists, of dissimilar sizes
    # You want to see how many entries in the one list are present in the other
    nplist6 = np.random.randint(0,20,10)
    nplist7 = np.random.randint(0,20,15)
    print(nplist6)
    print(nplist7)
    print(np.in1d(nplist6,nplist7))     # Result list is same dimension as 1st list
    # --------------------------------------------------------------------------
    # You have one array with numbers, with duplicates
    # You want a list, with maxn entries where maxn is the max_number if the array, with each entry as a count of how many times a number if found
    nplist8 = np.random.randint(0,20,10)
    print(nplist8)
    print(np.bincount(nplist8))
    # Variation - you want a parallel list to the original with just the count of each number found, not the long list
    print(np.bincount(nplist8)[nplist8])
    # --------------------------------------------------------------------------
    # You have one array with numbers
    # You want to negate all values between two numbers
    nplist9 = np.random.randint(0,20,10)
    print(nplist9)
    nplist9[(nplist9 > 3) & (nplist9 < 7)] *= -1
    print(nplist9)


# func_01()
# func_02()
func_03()
# func_04()
# func_05()