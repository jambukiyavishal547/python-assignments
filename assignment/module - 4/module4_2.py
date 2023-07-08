#Python program to read an entire text file
def read(fname):
        txt = open(fname)
        print(txt.read())

read('demo.txt')
