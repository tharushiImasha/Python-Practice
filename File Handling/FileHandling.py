file_1 = open("File Handling/my_file.txt", 'r')

# content = file_1.read()
# content = file_1.readline()
content = file_1.readlines()

print(content)
print(type(content))

file_1.close()