# Explaination: Lists are like a bucket storing data, it might contain username, email address, password.
# As you can see we got a list contact, which contains name, mail, address. We can fetch them in our code,
# We can add further or even remove them from a list. The for loop will I was using here is to print out each
# data stored in a list. 

contact = ["name", "mail", "address"]

for data in contact:
    print(data)



# EXTRA .. 

my_list = ["item1", "item2", "item3"]

for items in my_list:
    print(items[::-1] + " It was actually = " + items)
