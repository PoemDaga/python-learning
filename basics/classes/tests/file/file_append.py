lines = ["------This is a new line that I am adding to existing file\n", "\n------this is yet another line\n"]

with open("../data/file1.txt", "a") as file1:
    while lines:
        file1.write(lines.pop())

with open("../data/file1.txt", "r") as file1:
    file_data = file1.readlines()
    print(file_data)
