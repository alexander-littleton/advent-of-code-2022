import day3_1


def test_calculate_priorities():
    rucksacks = [
        {
            "compartment_1": "abc",
            "compartment_2": "aBC"
        },
        {
            "compartment_1": "abc",
            "compartment_2": "AbC"
        }
    ]
    assert day3_1.calculate_priorities(rucksacks) == 3


def test_make_rucksack():
    raw_rucksack = "abcABC"
    assert day3_1.make_rucksack(raw_rucksack) == {
        "compartment_1": "abc",
        "compartment_2": "ABC"
    }
