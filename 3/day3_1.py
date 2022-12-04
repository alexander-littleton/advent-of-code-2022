ALPHABET = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def extract_rucksacks():
    file = open("input.txt", "r")
    raw_rucksacks = file.readlines()
    rucksacks: list[dict[str, str]] = []
    for raw_rucksack in raw_rucksacks:
        rucksacks.append(make_rucksack(raw_rucksack))
    return rucksacks


def make_rucksack(raw_rucksack: str) -> dict[str, str]:
    compartment_size = int(len(raw_rucksack)/2)
    return {
        "compartment_1": raw_rucksack[:compartment_size],
        "compartment_2": raw_rucksack[compartment_size:]
    }


def calculate_priorities(rucksacks: list[dict[str, str]]) -> int:
    total_priorities = 0
    for sack in rucksacks:
        compartment_1 = sack["compartment_1"]
        compartment_2 = sack["compartment_2"]
        for char in compartment_1:
            if char in compartment_2:
                total_priorities += ALPHABET.index(char)
                break
    return total_priorities


print(calculate_priorities(extract_rucksacks()))
