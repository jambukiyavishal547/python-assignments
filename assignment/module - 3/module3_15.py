#Python program to get unique values from a list
unique_list = []
list1 = [10, 20, 10, 30, 40, 40]
	# traverse for all elements
for x in list1:
		# check if exists in unique_list or not
	if x not in unique_list:
                unique_list.append(x)
print("Unique list is: ",unique_list)