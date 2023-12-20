with open("../data/file1.txt", "r") as original:
    with open("../data/copyOfFile1.txt", "w") as copy:
        for line in original.readlines():
            copy.write(line)
