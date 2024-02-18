# Explaination: Variables are like bucket, we store our things in it. We can use those things anytime and we can replace them etc.
# We basically assign a value to variable and we can use that or re-call that value by simply calling variable.
# Example: variable = "Welcome to my code!" now instead of writing this whole sentence "Welcome to my code!", 
# I could just simply recall that variable like: print("Starting: {variable}"), Output: Starting: Welcome to my code!


# Variables. It holds some kind of data. This name variable is going to hold whatever is after = 
name = ("John Doe")
print(name)

# Using a variable within a variable.
data = ("Username: " + name)
print(data)

# Using F strings to add variables.
data = (f"Username: {name}")
print(data)

# Slicing, getting only what is required from data. A list starts from 0 for example, T is on 0.
data = ("Tommy")
print(data[0])

# Name your variables good! the input after = is basically getting input from the user and we are storing it in variable "data_required"
data_required = input("Please upload your data, required: ")
print(data_required)


# ------------------------------ CHALLENGE -------------------------------------

# Create an input with hello and ask favourite food, hobby. Print with a f string including food & hobby.

favourite_food = input("Hello! What is your favourite food? ")
favourite_hobby = input("What is your favourite hobby? ")
print(f"Favourite food: {favourite_food} and Favourite hobby: {favourite_hobby}")

