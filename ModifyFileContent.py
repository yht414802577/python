import fileinput

for line in fileinput.input("E:\\111.txt",inplace = 1):
	line = line.replace("qwe","123")
	print line


