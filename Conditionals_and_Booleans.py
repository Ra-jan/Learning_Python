# Conditionals helps to understand what statement gets executed depending on whether the certain values evaluate to True or False

"""Comparisons used in the conditional statement
Equal               ==
Not Equal           !=
Greater than         >
Less than            <
Greater or equal to  >=
Less or equal to     <=
Object identity      is
"""

# These all below values are evaluated to FALSE by the python compiler
""" False values
False
None
Zero of any numeric type ('0')
Any empty sequence. For Example '', (), []
Any empty mapping. For Example  {}
"""


# The conditional statement should always end with :
# Indentation has to be followed in the conditional statements.

# IF Conditions

if True:
    print('conditional was True')
# The next statement (in this case Print) will only execute when the IF statement is True

if False:
    print('conditional was False')
# We see that it didn't execute the print statement as the condition was False

# ELSE Conditions
# The conditional statement is executed when the first condition is False.

language = 'Python'
if language == 'Java':
    print('conditional was True')
else:
    print('conditional was False')
# Here the else block of the code is executed when the if conditional is False.

# ELIF Condition
# This conditional statement is executed when we have to check multiple conditions to be True or False

language = 'Python'
if language == 'Java':
    print('conditional was True')
elif language == 'Python':
    print('conditional was Python')
else:
    print('No Match')
# Here, the code goes through first iteration (IF) to check if the condition is True, if not then it goes to second iteration (ELIF) to check if it's True and give output. If both turns out to be False, it will go to the ELSE condition.
# we can keep on adding multiple elif statements, if we have multiple values to iterate through

language = 'Ruby'
if language == 'Java':
    print('Language is Java')
elif language == 'Python':
    print('Language is Python')
elif language == 'C++':
    print('Language is C++')
elif language == 'Ruby':
    print('Language is Ruby')
else:
    print('No Match')
# Here it goes upto 3 iterations where it found the True condition and executed the statement.

""" In addition to the comparisons, we can also use Boolean operations such as:
and
or
not
"""

user = "Admin"
Logged_in = True
if user == "Admin" and Logged_in:
    print("Logged in")
else:
    print("Not Logged in")
# Here, is we have multiple conditions to check, we can also use the boolean operations
# If one of the condition doesn't match, the iteration is considered to be False

user = "Admin"
Logged_in = False
if user == "Admin" and Logged_in:
    print("Logged in")
else:
    print("Not Logged in")
# Here even though the user condition is True the Logges in is False and hence it moves and executes the else statement.
# In AND operator, all the conditions checked should be TRUE

user = "Admin"
Logged_in = False
if user == "Admin" or Logged_in:
    print("Logged in")
else:
    print("Not Logged in")
# In OR operator, any one of the condition is to be True for the statement to execute.


user = "Admin"
Logged_in = False
if not Logged_in:
    print("Please Log in")
else:
    print("Welcome Admin")
# NOT operator is used to switch the boolean value, like here the logged in is set to False but when used in the if statement, it changed the value to True and hence it executed the statemnt

# IS keyword
# It tests if the 2 objects have same identity, which basically refers to checking if they are same object in memory
a = [1, 2, 3]
b = [1, 2, 3]
# Here is we use the == operator, it will give true as the value of both variables are same
print(a == b)

# But if we use the is operator, it gives us False because both a and b variables might be same in values but the id's they're stored in the memory is different.
# We can check the ID's with id()
print(id(a))
print(id(b))
print(a is b)
# Here we see the IDs they are stored in are different, hence a is not b.

# if we just do
b =  a
# and then execute the is operator, it will give true as the IDs will become the same
print(id(a))
print(id(b))
print(a is b)
# What is operator do is basically check if the id() == id()
print(id(a) == id(b))

