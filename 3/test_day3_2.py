import day3_2


def test_calculate_badge_priorities():
    rucksack_groups = [
        [
            "abc",
            "ade",
            "afg"
        ],
        [
            "bcd",
            "bef",
            "bgh"
        ],
    ]
    assert day3_2.calculate_badge_priorities(rucksack_groups) == 3
