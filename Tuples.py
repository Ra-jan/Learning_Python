# Tuples are very similar to lists but the only difference is it cannot be modified.
# Tuples are immutable
# Thw tuple is defined exactly as lists but in ()

# IMMUTABLE

tuple_1 = ('Python', 'Java', 'C++', 'Ruby', 'Go')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)

# we cannot make any changes in tuple as we did in the lists, hence it doesn't have a lot of functions/Methods as lists
''' EXAMPLE:
If we try to make change in the tuple as we did in list
tuple_1[0] = 'Art'
print(tuple_1)
print(tuple_2)

It will give us error as "Tuple does not support item assignment"
'''

# We cannot mutate the values such as append,remove etc. but we can access the values, iterate through values, loop through the tuple etc.

# To create empty tuples, we can use either of the means below:
empty_tuple = ()
empty_tuple_1 = tuple()
print(empty_tuple)
print(empty_tuple_1)