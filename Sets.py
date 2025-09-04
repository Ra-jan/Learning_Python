# Sets are values that are unordered and also have no duplicates
# It is defined same as lists but in {}

# Sets

courses = {"Python", "Java", "Physics", "Maths", "Python"}
print(courses)
# As many times you run this, you will see the output in different order, every time because unline lists and tuples, sets don't really care about order.
# The usage is mostly to check if the value is part of the set and also if there are no duplicate values.
# Even if Python value is added twice in the set, it only prints one in the output.

# To check if the value is present in the set
print('Python' in courses)
# It will print True or False depending on the result

# Sets are also used to determine what values they share with another sets with use of some methods

# To check duplicate values in 2 different sets, we will create new set and try this
# We will use .intersection() method to see what values are shared by these 2 sets
subjects = {"Python", "Science", "Physics", "SST"}
print(courses.intersection(subjects))
# Here it will print Python and Physics as they're shared/same in both the sets

# To check what values are unique in both the sets, we use .difference() method
print(courses.difference(subjects))
# Here it will print Maths and Java as we are checking values present in courses but not in subject
print(subjects.difference(courses))
# Here it will print SST and Science as we are checking values present in subjects and not in courses

# To combine both the sets together, we can use .union() method
print(courses.union(subjects))
# Even here the multiple time you print, the different output of print you will get as it will be unordered.

# To create empty sets, we can use either of the means below:
empty_set = set()
print(empty_set)
# We can't use empty_Set = {} as it will create a DICTIONARY instead of empty set. We will have to use built-in set() class to create empty sets.


