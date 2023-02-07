# A tuple in Python is similar to a list. The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list.

# Advantages of Tuple over List in Python
# Since tuples are quite similar to lists, both of them are used in similar situations.

# However, there are certain advantages of implementing a tuple over a list:

# We generally use tuples for heterogeneous(different) data types and lists for homogeneous(similar) data types.
# Since tuples are immutable, iterating through a tuple is faster than with a list. So there is a slight performance boost.
# Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
# If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.

# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3, [2, 3, 4])
print(my_tuple)

# tuple with mixed datatypes
my_tuple2 = (1, "Hello", 3.4)
print(my_tuple2)

# accessing tuple elements using indexing
letters = ("p", "r", "o", "g", "r", "a", "m", "i", "z")

# slicing
print(letters[2])   # prints "p"
# elements 2nd to 4th index
print(letters[1:4])  # prints ('r', 'o', 'g')

# count touple
print(letters.count('g'))

# Check if exist in list

print('c' in letters)    # False
print('o' in letters)    # True

# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'i', 'u')
# counts the number of i's in the tuple
count = vowels.count('i')
print(count)
