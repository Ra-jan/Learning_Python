#LEARNING STRINGS

# 1st program to just learn how to print
print("Hello, My name is Rajan Kumar")


# How to define a value to a variable. Here message variable hold the text data which is also known as strings.
message="Hello World"
print(message)

# \ is the escape character which can be used within the " & '.
# In the below example both strings are printed in the same way with the use of escape character and the use of "
# If the string contains ' in the message we use " on the outside and vice versa
message1 = 'Bobby\'s world'
print(message1)

message2 = "Bobby's world"
print(message2)

# To print multiline string in different line we use """ in the beginning and end of the string
msg3 = """Bob the builder
was a great cartoon 
back in our days"""
print(msg3)

# To print how many character are there in the string, we use len
msg4 = "Bob the builder"
print(len(msg4))

# To print the string characters individually we can use the [], the location of the character is called indexes which starts from 0 and so on.
msg5 = "Rajan is great"
print(msg5[6])
# To access the range of characters we use :
print(msg5[6:14])
# To print from start to any index we can use [:x] & to print from any index to end we can use [x:]

# To print the string in all lower case we use '.lower()' and for upper case we use '.upper()'
print(msg5.lower())
print(msg5.upper())

# To count the certain number of characters/words in string we use '.count('')'
print(msg5.count('Rajan'))
print(msg5.count('a'))

# To find the index where certain characters can be found we use '.find('')'
print(msg5.find('is'))
print(msg5.find('great'))

# To replace certain characters from the string with other characters we use '.replace('','')' in which first '' will contain the character/word to be replaced and the second will have the character to be replaced with.
print(msg5.replace('Rajan','Bittu'))

# or we can also do it with assigning the replacement to new variable
msg6 = msg5.replace('Rajan','Bittu')
print(msg6)

# To add multiple words and concatenate them together
greeting = 'Hello'
Name = 'Bittu'
Compliment = "You're absolutely amazing person and I LOVE YOU."

msg7 = greeting + ' ' + Name + ', ' + Compliment
print(msg7)

# We can also do this with the use of placeholders instead of using + sign, if the variables are too much then it would be a problem to + them together
# The {} takes the value of the variables in the order in which they're defined in the .format() method
msg8 = '{} {}, {}'.format(Name, greeting, Compliment)
print(msg8)

# This can also be done using fstrings but only in 3.6 version
msg9 = f'{greeting} {Name}, {Compliment}'
print(msg9)

# This is beneficial as you can add method inside the placeholder of fstrings
msg10 = f'{greeting} {Name.upper()}, {Compliment}'
print(msg10)

#To conclude, i have learnt about Strings

