#program to unzip a list of tuples into individual lists
# Unzip a list of tuples
l= [('my', 1), ('name', 2), ('is', 3), ('vishal', 4)]

# Printing original list
print("Original list is : " + str(l))

# using list comprehension to
# perform Unzipping
result = [[i for i, j in l],
	  [j for i, j in l]]

# Printing modified list
print("Modified list is : " + str(result))
