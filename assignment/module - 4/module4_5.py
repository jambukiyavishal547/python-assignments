#a Python program to read last n lines of a file
def LastNlines(fname, N):
	with open(fname) as file:
		for line in (file.readlines() [-2:]):
			print(line, end ='')

if __name__ == '__main__':
	fname = 'demo.txt'
	try:
		LastNlines(fname,-2)
	except:
		print('File not found')
