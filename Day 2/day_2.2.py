text = open("day_2.txt", "r")
bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}
bagIndex = {
    "red": 0,
    "green": 1,
    "blue": 2
}
total = 0
game_id = 1

for line in text:
    minList = [0, 0, 0]
    splitLine = line.rstrip().replace(',', '')
    splitLine = splitLine.replace(';', '')
    splitLine = splitLine.split(' ')[2:]

    for i in range(1, len(splitLine), 2):
        if minList[bagIndex[splitLine[i]]] < int(splitLine[i - 1]):
            minList[bagIndex[splitLine[i]]] = int(splitLine[i - 1])

    total += minList[0] * minList[1] * minList[2]

print(total)
text.close()
