file = open("jan13_2.txt", 'w')
file.write("This is a new file")

file = open("jan13_2.txt",'r')
content = file.read()
print(content)

file = open("jan13_2.txt", 'a')
file.write("This line is appended.")


file = open("jan13_2.txt", 'r+')
content = file.read()
file.write("python programming\n")

file = open("jan13_2.txt",'r')
print(file.read())

file = open("jan13_2.txt", 'a+')
file.write("object oriented programming")
file.seek(0)
content = file.read()
print(content)
