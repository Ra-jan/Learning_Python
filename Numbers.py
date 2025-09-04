# Here I learn about the numbers (Strings, Float, Complex)


# Integer is a whole number and Float represents the decimal.
num = 3
print(num)
num1 = 4.5
print(num1)

# To check the type of the data, we use type()
print(type(num))
print(type(num1))

# Arithmetic Operators:
# Addition:             3 + 2
# Subtraction:          3 - 2
# Multiplication:       3 * 2
# Division:             3 / 2
# Floor Division:       3 // 2
# Exponent:             3 ** 2
# Modulus:              3 % 2 - Gives us remainder of division

# To increment a value of the variable
n = 1
n = n + 1
print(n)

# Or we can also use '+='
# Same can be used for '*=',
n += 1
print(n)

# 'abs' absolute value is used to disregard the - & = sign
print(abs(-4))

# 'round' is used to round the number to nearest integer value
print(round(4.78))

#Comparison Operators:
# Equal:                 3 == 2
# Not Equal:             3 != 2
# Greater than:          3 > 2
# Less than:             3 < 2
# Greater or Equal:      3 >= 2
# Less or Equal:         3 <= 2


# If the numbers are entered within '' and "", then python will consider it as strings
n1 = '100'
n2 = "200"
print(n1 + n2)

# To make python consider it as number, we have to do casting
n1 = int(n1)
n2 = int(n2)
print(n1 + n2)