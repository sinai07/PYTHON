# This is my first project with Python
# Create variable for my Services list:
a = "S3"
b = "Lambda"
c = "EC2"
d = "ELB"
e = "cloudformation"

# Create an empty list:

my_list = []

# Create a new list with all the services added using append:
my_list.append(a)
my_list.append(b)
my_list.append(c)
my_list.append(d)
my_list.append(e)

# Print my new list and len of list:
print(my_list)
print(len(my_list))

# Delete tho services by index:
del my_list[1:4]

# Print updated list and len of list:
print(my_list)
print(len(my_list))