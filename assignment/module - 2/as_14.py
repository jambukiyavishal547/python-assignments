#count the number of characters (character frequency) in a string
st ="abcd abc ab" #input("Input stirng: ")
res = {i: st.count(i) for i in set(st)}
print("all characters is :\n "+ str(res))
