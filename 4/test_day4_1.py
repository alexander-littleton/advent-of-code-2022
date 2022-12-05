import day4_1


def test_count_fully_overlapping_pairs():
    input = [
        [
            [0, 4],
            [0, 2]
        ],
        [
            [3, 4],
            [4, 6]
        ],
        [
            [0, 1],
            [2, 3]
        ]
    ]
    assert day4_1.count_fully_overlapping_pairs(input) == 1
