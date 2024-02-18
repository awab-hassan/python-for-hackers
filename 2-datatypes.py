# Strings are link, think of "words" you write, like "hello" or "Python is fun!" They store text you can see and use.
# Integers are like whole numbers for counting, like 10 apples or -5 degrees. They hold exact, non-decimal numbers.
# floats are like  numbers with decimals, like 3.14 (pi) or 2.71 (e). They represent decimal values.
# Booleans are like a light switch, they can be either True (on) or False (off). They answer yes/no questions in your code.


# Strings. (Anything between quotations in python is considered as string.)
string = "basic string"

# Integers. (Basically numbers)
integer = 10

# floats. (number with . )
floats = 10.10

# Booleans.
booleans = ("Either true or false")

# --------------------- CHALLENGE -----------------------

# Add num1 + num2, Add second number in num1 and in num3, Change num2 into a float and print the type to console as float.

# Solution 1

num1 = "12345"
num2 = "678910"
num3 = "111213"

first_addition = (int(num1) + int(num2))
second_addition = (first_addition + int(num1))
third_addition = (first_addition + int(num3))
converting_to_float = float(num2)
print(type(converting_to_float))

# Solution 2

num1 = "12345"
num2 = "678910"
num3 = "111213"

print(int(num1) + int(num2))
print(num2[1] + num3[1])
print(type(float(num2)))