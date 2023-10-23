# Count repiat the sub string 
main_str ="abcde abcd abc"   #input("Enter string: ")
sub_str ="ab"  #input("Enter sub string: ")

res = sum(1 for i in range(len(main_str))
		if main_str.startswith(sub_str, i))
print("Number of substrings", res)
