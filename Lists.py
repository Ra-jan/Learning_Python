# List and Tuples allow us to work with sequential data
# Lists are mutable
# Sets are unordered collection of values with no duplicates.

#LISTS is defined in [] with each value separated by COMMA (,)
courses = ["Python", "Java", "C++", "Ruby", "Go"]
print(courses)

# To get how many values are in the list, we can use len()
print(len(courses))

# To access each values individually, we can specify indexes
print(courses[2])
print(courses[4])
# To access them individually in reverse order, we can use negative indexes.
print(courses[-2])
print(courses[-5])

# We can also access the range of values using the index
print(courses[0:3])
# The last index is exclusive, whatever 'n' is mentioned there, python considers it n-1.


# LIST METHODS


# To add any item in the last of the list, we use .append('x')
courses.append("HTML")
print(courses)

# To add any item in any specific place, we use .insert(x,'y') - where x is the index where the value is to be inserted and y is the value itself
courses.insert(3, 'PHP')
print(courses)

# To add multiple values in the list, we use .extend(variable)
subject = ["Maths", "Science" ]
courses.extend(subject)
print(courses)

# To remove values from the list, we use .remove()
courses.remove("Maths")
print(courses)

# We can also use .pop(), it will automatically remove the last item in the list ,and it can also print the popped value
popped = courses.pop()
print(courses)
print(popped)

# To reverse the list, we use .reverse()
courses.reverse()
print(courses)

# To sort the list, we use .sort(), it will sort alphabetically
courses.sort()
print(courses)
# If it contained numbers, it would sort in ascending order
num = [1, 6, 3, 7, 2, 9, 12, 101, 34]
num.sort()
print(num)
# To do it in descending order, we use reverse method in sort
num.sort(reverse=True)
print(num)
courses.sort(reverse=True)
print(courses)

# To get the sorted list without altering the original, we use sorted() function
# Sorted function doesn't sort in place, it returns a sorted version of the list and to fetch that we have to assign it a new variable
course = sorted(courses)
print(course)

# To get the minimum from the numbers list, we use min()
print(min(num))
# To get the max from the numbers list, we use max()
print(max(num))
# To get the sum of the numbers list, we use sum()
print(sum(num))

# To find the index of a value from the list, we use .index('value')
print(courses.index('Ruby'))
# To check if the value is present in the list, we use 'in' operator
print('Maths' in courses)
print('C++' in courses)

# To print out each item from the list, one by one we can use a for loop
for item in courses:
    print(item)
# It prints each of them in a new line because print statement goes to a new iteration each time it executes in the loop

# To print the index and items from the list, we use enumerate() function
for index, item in enumerate(courses):
    print(index, item)


# To start the index value from any particular number , we can define in the enumerate function
for index, item in enumerate(courses, start=9):
    print(index, item)


# To print your list in form of string with separations, we can use .join(variable)
course_str = ', '.join(courses)
print(course_str)
course_str1 = ' - '.join(courses)
print(course_str1)
# Whatever we give in the '' before .join(), it will work as a separator in the list when it is being converted into series of strings


# We can also split the string and create it into lists using .split('- or ,') where () will contain the separator
new_list = course_str.split(', ')
print(new_list)
new_list1 = course_str.split(' - ')
print(new_list1)

# Mutable
list_1 = ['history', 'Maths', 'Physics']
list_2 = list_1
print(list_1)
print(list_2)
# Here both of the list are same and are printed as such.
# Now, if we were to make change in any one of the list such as

list_1[0] = 'Art'
# Making change in the list, that's what makes it mutable
print(list_1)
print(list_2)
# Now if we print the list, it will give the output with the mutated(changed) data.


