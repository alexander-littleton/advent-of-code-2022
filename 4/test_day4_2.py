import day4_2


def test_count_overlapping_pairs():
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
        ],
        [
            [10, 20],
            [20, 30]
        ],
        [
            [19, 19],
            [19, 20]
        ],
        [
            [19, 20],
            [20, 20],
        ]
    ]
    assert day4_2.count_overlapping_pairs(input) == 5
