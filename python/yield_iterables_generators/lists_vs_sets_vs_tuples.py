'''
Sets are significantly faster when it comes to determining if an object is present in the set (as in x in s), but are slower than lists when it comes to iterating over their contents

When you want to store some values which you'll be iterating over or accessing by random index, Python's list constructs are slightly faster.
However, if you'll be storing (unique) values in order to check for their existence, then sets are significantly faster

Tuples are like lists, except they are immutable, in that they cannot be extended or reduced after creation.
But, if that is accecptable, tuples are faster than lists for iterations or access via random index.
While a tuple is immutable, you can always change a value in a tuple at an index.

Set CANNOT have duplicates - any duplicates during set creation are "merged" into 1 entry
Set Order is ARBITRARY (unlike lists, and like dicts)
'''

# Lists are enclosed in SQUARE brackets
aList = [1,2,3,4,5]

# Sets are created using the set function, and printed with CURLY brackets
aSet1 = set((1,2,3,4,5))    # Preferred
# Or
aSet2 = set([1,2,3,4,5])

# Tuples are enclosed in ROUND brackets
aTuple = (1,2,3,4,5)

print(aList,aSet1,aTuple)
print(aSet2)

# Set CANNOT have duplicates - any duplicates during set creation are "merged" into 1 entry
aSet3 = set([1,1,1,2,3,4])
print(aSet3)

