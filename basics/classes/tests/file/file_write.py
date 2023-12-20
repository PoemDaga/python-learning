lines =["Hey there!\n", "I am a Poem\n", "Writing to a file\n"]

with open("../data/newFile.txt", 'w') as file1:
    for line in lines:
        file1.write(line)


