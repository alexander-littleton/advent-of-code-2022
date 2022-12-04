import math

def extractAndTransformRounds():
    file = open("input.txt", "r")
    rawRounds = file.readlines()
    rounds = []
    for rawRound in rawRounds:
        rounds.append(makeRound(rawRound))
    return rounds

opponentChoiceMap = {
    'A': "rock",
    'B': "paper",
    'C': "scissors"
}

myChoiceMap = {
    'X': "rock",
    'Y': "paper",
    'Z': "scissors"
}

hierarchyMap = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

scoreMap = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

resultMap = {
    "W": 6,
    "D": 3,
    "L": 0
}

round = dict[str, str]

def makeRound(rawRound: str) -> round:
    opponentChoice = opponentChoiceMap[rawRound[0]]
    myChoice = myChoiceMap[rawRound[2]]
    result = ""
    if hierarchyMap[myChoice] == opponentChoice:
        result = "W"
    elif hierarchyMap[opponentChoice] == myChoice:
        result = "L"
    else:
        result = "D"

    return {
        "myChoice": myChoice,
        "result": result
    }

def calculateScore(rounds: round) -> int:
    score = 0
    for round in rounds:
        result = round["result"]
        myChoice = round["myChoice"]
        score += resultMap[result]
        score += scoreMap[myChoice]
    return score

print(calculateScore(extractAndTransformRounds()))