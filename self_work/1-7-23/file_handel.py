# Create a new file and write to it
file = open('example.txt', 'w')
file.write('This is a sample text.')
file.close()

# Read data from a file
file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()

# Update data in a file
file = open('example.txt', 'w')
file.write('This is the updated text.')
file.close()

# Delete a file
#import os
#os.remove('example.txt')