# Explaination: if, elif(else-if), else statements are used to perform actions according to situation in your code.
# For example we ask user to input a number and if user entered a number 10, we assign our code to such and such thing.
# Example: if age: 5 -> You are a kid.

# If you are under 5 you are a kid
# If you are 5-15 you are a big kid
# If you are 5-21 you are a bigger kid
# If you are over 21 you are old 

age = int(input("What is your Age? "))

if age < 5:
    print("You are a kid")
elif age == 5 or age < 16:
    print("You are a big kid")
elif age == 5 or age < 22:
    print("You are a bigger kid")
elif age > 21:
    print("You are old")


# ------------- CHALLENGE ---------------

# ask the user for the temprature input
# if its less than 20 degress you need boots
# if its less than 30 you need a coat
# if its less than 70 you need a jacket
# if its over 70 it is nice outside

temprature = int(input("What is the temprature right now? "))

if temprature < 20:
    print("You need boots")
elif temprature < 30:
    print("You need a coat")
elif temprature < 70:
    print("You need a jacket")
elif temprature > 70:
    print("It is nice outside")