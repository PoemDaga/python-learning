with open("../data/file1.txt", "r") as file1:
    fileStuff = file1.read()  # reads all lines as a single string
    print("File content:: ", fileStuff)

print("Is file closed?", file1.closed)
print("File name:", file1.name)
print("File mode:", file1.mode)  # file name
print("File content after closing:: ", fileStuff)

# fileStuff = file1.read()      # ValueError: I/O operation on closed file.


print("-------------------")
with open("../data/file1.txt", "r") as file1:
    lines = file1.readlines()  # reads all lines as a list
print("file lines:", lines)

print("-------------------")
with open("../data/file1.txt", "r") as file1:
    first_line = file1.readline()  # reads 1 (first) line as a string
    second_line = file1.readline()
print("file first line:", first_line)
print("file second line:", second_line)
if 'This' in second_line:
    print("files second line has this keyword:", second_line)

print("-------------------")
with open("../data/file1.txt", "r") as file1:
    while True:
        line = file1.readline()
        if not line:
            # print(f"no more lines: '{line}'")
            break  # Stop when there are no more lines to read
        print(line)
