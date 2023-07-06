# Python program to remove an empty tuple(s) from a list of tuples
tuples = [(), ('ram'), (), ('laxman'),('krishna'), (),()]
tuples = [t for t in tuples if t]
print(tuples)
