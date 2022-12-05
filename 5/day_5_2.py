from typing import TypedDict

Stack = list[str]

stacks: list[Stack] = [
    ['N', 'B', 'D', 'T', 'V', 'G', 'Z', 'J'],
    ['S', 'R', 'M', 'D', 'W', 'P', 'F'],
    ['V', 'C', 'R', 'S', 'Z'],
    ['R', 'T', 'J', 'Z', 'P', 'H', 'G'],
    ['T', 'C', 'J', 'N', 'D', 'Z', 'Q', 'F'],
    ['N', 'V', 'P', 'W', 'G', 'S', 'F', 'M'],
    ['G', 'C', 'V', 'B', 'P', 'Q'],
    ['Z', 'B', 'P', 'N'],
    ['W', 'P', 'J']
]


def extract_directions():
    file = open("input.txt")
    return file.readlines()


class Direction(TypedDict):
    amount: int
    origin: int
    destination: int


def transform_directions(raw_directions: list[str]) -> list[Direction]:
    directions: list[Direction] = []
    for raw_direction in raw_directions:
        split_direction = raw_direction.split(" ")
        amount = int(split_direction[1])
        origin = int(split_direction[3])-1
        destination = int(split_direction[5])-1
        direction: Direction = {
            "amount": amount,
            "origin": origin,
            "destination": destination
        }
        directions.append(direction)
    return directions


def execute_directions_on_stacks(directions: list[Direction], stacks: list[Stack]) -> list[Stack]:
    for direction in directions:
        amount = direction['amount']
        origin = stacks[direction['origin']]
        destination = stacks[direction['destination']]

        moving = origin[len(origin)-amount:]
        origin = origin[:len(origin)-amount]

        # i love python
        stacks[direction['destination']] = destination + moving
        stacks[direction['origin']] = origin

    return stacks


def get_message_from_stacks(stacks: list[Stack]) -> str:
    message = ''
    for stack in stacks:
        if len(stack) > 0:
            message = message + stack[::-1][0]
    return message


print(get_message_from_stacks(execute_directions_on_stacks(
    transform_directions(extract_directions()), stacks)))
