# Loops are used to loop through strings, list etc

# FOR Loop

nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)
# This basically makes the code loop through each value defined in variable nums and print it.
# This will print the value sequentially in the new lines


# 2 Important keywords while working with loops are
# BREAK keyword will completely break out of the loop
# CONTINUE keyword will move to the next iteration.

nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print("found it")
        break
    print(num)
# This will run the iteration till the if condition is satisfied and once it is, it will completely break out of the loop and end the iterations.

nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print("found it")
        continue
    print(num)
# This will run the iterations of for loop and when the conditional is met, it will print the output and then continue to the next iteration.
# Continue is also used to skip through iterations

# LOOP within LOOP
for num in nums:
    for letter in 'abc':
        print(num, letter)
# Here we have a loop within the loop, it will run though each iteration and print each number with each string value


# If we want to run through a loop a certain number of times, we will use range()
for i in range(10):
    print(i)
# Here it will run the loop for 10 iteration, and print the output
# The number defined in the range is always exclusive, so it will print upto (n-1) times

# If we want the loop to start from a certain point, we can define that in range
for i in range(1, 11):
    print(i)
# Here it will print from 1 to 10 as 11 is exclusion

for i in range(1, 10, 2):
    print(i)
# Here we are looping through range of 1 to 10 while printing every 2nd number.
# We can define which number to be printed as such
# Here, we print every 4th number
for i in range(0, 20, 4):
    print(i)


# WHILE Loops
# These loops can go on iterations for as long as the conditional/criteria is met, or we hit BREAK

x = 0
while x < 10:
    print(x)
    x += 1
# Here the value of x is defined and the loop is to run till the criteria x<10 is met.
# We gave the last iteration +=, so that number keeps on increasing in the loop or the loop will run continuously

# We can use break to end the iteration at any time we want
x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1
# Here we have instructed the code to break once the conditional in the loop is met

x = 0
while x < 10:
    x += 1
    if x == 5:
        print("got 5")
        continue
    print(x)
# Here we used the continue keyword to print the "Got 5" when the conditional was met and skip that number and proceed further
# Also, x+=1 is defined before the conditional because if not, the loop will run infinite times
