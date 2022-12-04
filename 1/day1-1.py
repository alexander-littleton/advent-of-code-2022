def parseElves():
    inputFile = open('input.txt', "r")
    calorieData = inputFile.readlines()
    inputFile.close()
    caloriesPerElf: list[int] = []
    currentElf = 0
    for line in calorieData:
        if line != '\n':
            currentElf += int(line)
        else:
            caloriesPerElf.append(currentElf)
            currentElf = 0
    print(max(caloriesPerElf))


parseElves()
