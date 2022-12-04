ALPHABET = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def extract_rucksack_groups():
    file = open("input.txt", "r")
    raw_rucksacks = file.readlines()
    rucksack_groups: list[list[str]] = []
    for i in range(len(raw_rucksacks))[::3]:
        rucksack_group = [
            raw_rucksacks[i],
            raw_rucksacks[i+1],
            raw_rucksacks[i+2]
        ]
        rucksack_groups.append(rucksack_group)
    return rucksack_groups


def calculate_badge_priorities(rucksack_groups: list[list[str]]) -> int:
    total_priorities = 0
    for group in rucksack_groups:
        rucksack_1 = group[0]
        rucksack_2 = group[1]
        rucksack_3 = group[2]
        for item in rucksack_1:
            if item in rucksack_2 and item in rucksack_3:
                total_priorities += ALPHABET.index(item)
                break
    return total_priorities


print(calculate_badge_priorities(extract_rucksack_groups()))
