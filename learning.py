
# 4 core data types:

# Int
from tkinter import _XYScrollCommand


7
-26473

# Float
6.8
456.268

# String
'Hello'
"I am 17"
a = 'Hello'
b = 'I am 17'
print(a + b)




# Bool
True 1
False 0



# Output:

print('Hello World!')
print(4.5)
print(4.5, 'Hello', False, end='\n')



# Variables:

my_name = 'cassius'
print(my_name)
age = 17
print(my_name, age)
# Note, value changes occur in line order



# User input:

name = input('Name: ')
age = input('Age: ')
print('Hello', name, 'you are', age, 'years old.')



# Arithmetic operators:

x = 9
y = 3
result = int(x / y) # Here we are converting result from float to integer
print(result)
x // y # Gives integer of division
x % y  # Gives remainder
num = input('Number: ') # Always gives string values, not int
print(int(num) - 5)



# String methods:

hello = 'hello' .upper # Prints string in upper case
print(hello)
print(hello.lower) 
print(hello.capitalize)
print(hello.count('ll')) # Will count how many 'll's are in the string



# Conditional operators:

x = 'hello'
y = "hello"
print(x == y) # Will say if they are equal or not (true or false)
print(7.5>7)

# Chained conditionals:

result1 = x == y
result2 = x > y
result3 = x != y
result4 = result1 or result2 or not result3 # Gives true if any of these are true
print(result4)
print(not False) # Gives true
# Order of conditionals: not, and, or




# if/else/elif:

x = input('Name: ')
if x == 'Cassius':
    print('You are the best')
elif x == 'Hagrid': # For when you want more than one 'if' statement. Must come between an if and an else.
    print('Gay')
else: 
    print('You are average') # Prints something else if the 'if' condition is not met





# List/Tuples:
x = [4, True, 'hi'] # Square brackets means this is a list and can be altered
y = 'hi'
print(len(x) + len(y))
x.append('hello') # Adds element to the end of the list
x.extend(4,5,5,5,5) # Adds all elements to end of list
print(x.pop()) # Removes last element of list
x.pop(0) # Removes index (first element)
print(x[1]) # Prints specific element (index form)
z = (0,0,2,2) # Tuple (normal brackets), cannot be altered 


# For loops:

for i in range(10): # i for integer
    print(i)
# 1 value in range function = stop
# 2 values = start, stop
# 3 values = start, stop, step
for i in range(1, 17, 2):
    print(i) 
# Will go from 1 to 16 with jumps of 2

x = [1,4,4,3,5,7]
for i, element in enumerate(x):
    print(i, element) # Creates indexes and values for each element in list



# While loops:

i = 0
while i < 10:
    print('run')
    i += 1 # Will print 'run' 10 times
    if i ==10:
        break



# Slice operator:

x = [0,4,4,2,2,5,7,8]
y = ['hello', 'hi', 'goodbye', 'bye', 'morning']
sliced = x[0:4:2] # Start, stop, step
sliced = x[:5]
sliced = y[::-1] # Reverses order of list



# Sets:

s = set(1,4,56,72,8)
print(5 in s) # Checks if 5 is in the set (T or F)
s2 = {1,2,58,3,5}
print(s.union(s2))


