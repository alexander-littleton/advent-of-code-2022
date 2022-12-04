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

    sumOfTopThree = 0
    for i in range(3):
        sumOfTopThree += max(caloriesPerElf)
        caloriesPerElf.remove(max(caloriesPerElf))
    print(sumOfTopThree)


parseElves()
