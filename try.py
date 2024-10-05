from sys import argv

# print(argv)
if len(argv) < 2:
    print("Please provide a filename")
else:
    file = open(argv[1])
    print(file)
    lines = file.read()

    print(type(lines))
    print(lines)
    lines = lines.split("\n")
    line_count = len(lines)
    word_count = 0
    letter_count = 0
    for line in lines:
        words = line.split(" ")
        word_count += len(words)
        letter_count += len(line)

    print(lines)

    print("line count:", line_count)
    print("word count:", word_count)
    print("letter count:", letter_count)
