# Dictionaries allow us to work with key : Value pairs
# Key : Value pair is a linked values where the key is the unique identifier where we can find the data and value is the data.

# The dictionary is represented by {}
# The Key & values in the dictionary can be anything such as int, float, string, list etc.

student = {'name' : 'John', 'age' : 25, 'courses' : ['Maths', 'Physics']}
print(student)


# To print all the keys in the dictionary
print(student.keys())
# To print all the values in the dictionary
print(student.values())
# To print keys along with the values
print(student.items())

# Here, The name and age is key and JOHN and 25 is value. To separate the key : Value pairs we use ,.
# We can also define Lists, Tuples and sets inside a dictionary.
# Normal print will show the whole data in the dictionary.

# To print value of a particular key , we use dictionary_variable['key']
print(student['name'])
print(student['courses'])
# If we try to access a value of the key which doesn't exist, we get 'KeyError'
# If we don't want to get the error while accessing the value of key that doesn't exist, we use .get('key')
# When the .get method is used and the key : value pair doesn't exist, it will give output as None

print(student.get('age'))
print(student.get('Phone'))

# We can also specify the default value to return if the key is not found.
print(student.get('Address', 'Not found'))
# Now it will return 'NOT FOUND' instead of None for the address key

# we can also insert new key value to existing dictionary by below method
student['Phone'] = '1234-5678'
print(student.get('Phone'))

# If a key already exists and if we set new value, it will update the value of the key
student['name'] = 'jane'
print(student.get('name'))
print(student)
# This updated the name from JOHN to JANE

# We can also update values using .update({'' : ''}).
# Using .update we can update multiple values in the dictionary
# When we do the .update(), we have to define it as a new dictionary in the .update

student.update({'name': 'Bittu', 'age': 27})
print(student)
# This updated the name and age of the existing dictionary

# To delete a specific key from the dictionary, we use del keyword
del student['Phone']
print(student)

# Another way to remove a key is with .pop() method
courses = student.pop('courses')
print(student)
print(courses)
# This allows the user to also see the popped key , same as with lists
# but to return the popped key, we will have to assign the iteration with a variable

# To check how many keys we have in our dictionary, we can use .len() method
print(len(student))

# To loop through the items in the dictionaries
# If we use .items() , it will return the pair of key:value
for key, value in student.items():
    print(key, value)
# Normal for loop will only return the keys of the dictionary
for key in student:
    print(key)
for value in student:
    print(value)

# If we use .key and .values with dictionary, then we will get the respective data
for value in student.values():
    print(value)
for key in student.keys():
    print(key)

# Even if we use single key or value in for loop with .items(), we get the pairs
for key in student.items():
    print(key)
for value in student.items():
    print(value)

