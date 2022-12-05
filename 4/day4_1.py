def extract_assignment_pairs() -> list[list[list[int]]]:
    file = open("input.txt", "r")
    raw_assignment_pairs = file.readlines()
    assignment_pairs: list[list[list[int]]] = []
    for raw_pair in raw_assignment_pairs:
        raw_first_pair, raw_second_pair = raw_pair.split(",")

        raw_first_pair = raw_first_pair.split("-")
        first_pair: list[int] = []
        first_pair.append(int(raw_first_pair[0]))
        first_pair.append(int(raw_first_pair[1]))

        raw_second_pair = raw_second_pair.split("-")
        second_pair: list[int] = []
        second_pair.append(int(raw_second_pair[0]))
        second_pair.append(int(raw_second_pair[1]))

        assignment_pairs.append([first_pair, second_pair])

    print(assignment_pairs)
    return assignment_pairs


def count_fully_overlapping_pairs(assignment_pairs: list[list[list[int]]]) -> int:
    overlapping_pairs = 0
    for pair in assignment_pairs:
        first_pair = pair[0]
        second_pair = pair[1]
        if second_pair[0] >= first_pair[0] and second_pair[1] <= first_pair[1]:
            overlapping_pairs += 1
        elif first_pair[0] >= second_pair[0] and first_pair[1] <= second_pair[1]:
            overlapping_pairs += 1
    return overlapping_pairs


print(count_fully_overlapping_pairs(extract_assignment_pairs()))
