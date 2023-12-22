
print("-------------------")
with open("../data/file1.txt", "r") as file1:
    first_line = file1.readline(6)  # reads 1 (first) line as a string
    second_line = file1.readline()
print("file first line:", first_line)
print("file second line:", second_line)

