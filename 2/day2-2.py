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

necessaryResultMap = {
    'X': "L",
    'Y': "D",
    'Z': "W"
}

hierarchyMap = {
    "L": {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    },
    "W": {
        "paper": "scissors",
        "rock": "paper",
        "scissors": "rock"
    }
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
    necessaryResult = necessaryResultMap[rawRound[2]]

    return {
        "necessaryResult": necessaryResult,
        "opponentChoice": opponentChoice
    }

def calculateScore(rounds: round) -> int:
    score = 0
    for round in rounds:
        necessaryResult = round["necessaryResult"]
        opponentChoice = round["opponentChoice"]

        myChoice = ""
        if necessaryResult == "D":
            myChoice = opponentChoice
        else :
            myChoice = hierarchyMap[necessaryResult][opponentChoice]
        score += resultMap[necessaryResult]
        score += scoreMap[myChoice]
    return score

print(calculateScore(extractAndTransformRounds()))