# Python program to replace last value of tuples in a list.
l = [("a","b","c","d")]
print([t[:-1] + ("v",) for t in l])
