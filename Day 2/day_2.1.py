text = open("day_2.txt", "r")
bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}
total = 0
game_id = 1
for line in text:
    splitLine = line.rstrip().replace(',', '')
    splitLine = splitLine.replace(';', '')
    splitLine = splitLine.split(' ')[2:]
    check = True
    for i in range(1, len(splitLine), 2):
        if not (int(splitLine[i - 1]) <= bag[splitLine[i]]):
            check = False
            break

    if check:
        total += game_id
    game_id += 1

print(total)
text.close()
