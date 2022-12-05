import day_5_1


def test_transform_directions():
    raw_directions: list[str] = [
        'move 2 from 4 to 6',
        'move 10 from 9 to 5',
        'move 3 from 2 to 4',
        'move 8 from 4 to 7',
        'move 2 from 9 to 7'
    ]
    assert (day_5_1.transform_directions(raw_directions) == [
        {
            'amount': 2,
            'origin': 3,
            'destination': 5
        },
        {
            'amount': 10,
            'origin': 8,
            'destination': 4
        },
        {
            'amount': 3,
            'origin': 1,
            'destination': 3
        },
        {
            'amount': 8,
            'origin': 3,
            'destination': 6
        },
        {
            'amount': 2,
            'origin': 8,
            'destination': 6
        },
    ]
    )


def test_execute_directions():
    stacks: list[day_5_1.Stack] = [
        ['A', 'B', 'C', 'D', 'E'],
        ['F', 'G', 'H', 'I', 'J']
    ]
    directions: list[day_5_1.Direction] = [
        {
            'amount': 5,
            'origin': 0,
            'destination': 1
        },
        {
            'amount': 10,
            'origin': 1,
            'destination': 0
        }
    ]

    assert day_5_1.execute_directions_on_stacks(directions, stacks) == [
        ['A', 'B', 'C', 'D', 'E', 'J', 'I', 'H', 'G', 'F'],
        []
    ]


def test_get_message_from_stacks():
    stacks: list[day_5_1.Stack] = [
        ['A', 'B'],
        [],
        ['A'],
        ['B', 'A', 'C']
    ]

    assert day_5_1.get_message_from_stacks(stacks) == 'BAC'
