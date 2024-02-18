# Explaination: Lets say you want your programm to keep running until a User himself input's something which breaks the loop.
# I assigned a boolean "True" to a variable called on. Assigned 0 to a variable called count. As you can see the programm will keep running.
# Until a user enters something other than Y. 


on = True 
count = 0

while on:
    var = input("Continue this loop? Y/N ")
    if var == "y":            
        count += 1
        print(count)
    elif var != "y":
        on = False 
        