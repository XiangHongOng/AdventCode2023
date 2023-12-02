text = open("day_1_text.txt", "r")

total = 0
word2num = {
    "one": 'o1e',
    "two": 't2o',
    "three": 't3e',
    "four": 'f4r',
    "five": 'f5e',
    "six": 's6x',
    "seven": 's7n',
    "eight": 'e8t',
    "nine": 'n9e'
}
for line in text:
    print(line)
    for word in word2num:
        if word in line:
            line = line.replace(word, word2num[word])
    print(line)
    first, last = '', ''
    firstChecked, lastChecked = False, False
    for index in range(len(line)):
        if line[index].isdigit() and not firstChecked:
            first = line[index]
            firstChecked = True
        if line[len(line) - 1 - index].isdigit() and not lastChecked:
            last = line[len(line) - 1 - index]
            lastChecked = True
        if firstChecked and lastChecked:
            break
    print(int(first + last))
    total += int(first + last)
print(total)

text.close()
