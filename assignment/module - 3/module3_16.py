#Python program to check whether a list contains a sub list
test_list = [5, 6, 3, 8, 2, 1, 7, 1]

# printing original list
print("The original list : " + str(test_list))

# initializing sublist
sublist = [8, 2, 1]
print(sublist)
# Check for Sublist in List
# Using loop + list slicing
res = False
for i in range(len(test_list) - len(sublist) + 1):
	if test_list[i: i + len(sublist)] == sublist:
		res = True
		break
# printing result
print("Is sublist present in list ? : " + str(res))