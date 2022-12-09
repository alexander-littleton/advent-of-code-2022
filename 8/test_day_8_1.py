import day_8_1


def test_transform_forest():
    raw_forest: list[str] = [
        "01",
        "23"
    ]

    expected_forest: day_8_1.Forest = [
        [
            {
                "height": 0,
                "visible": False
            },
            {
                "height": 1,
                "visible": False
            },
        ],
        [
            {
                "height": 2,
                "visible": False
            },
            {
                "height": 3,
                "visible": False
            },

        ]
    ]

    assert day_8_1.transform_forest(raw_forest) == expected_forest


def test_assign_visible_linearly():
    forest: day_8_1.Forest = [
        [
            {
                "height": 0,
                "visible": False
            },
            {
                "height": 1,
                "visible": False
            },
        ],
        [
            {
                "height": 3,
                "visible": False
            },
            {
                "height": 2,
                "visible": False
            },

        ]
    ]

    expected_forest: day_8_1.Forest = [
        [
            {
                "height": 0,
                "visible": True
            },
            {
                "height": 1,
                "visible": True
            },
        ],
        [
            {
                "height": 3,
                "visible": True
            },
            {
                "height": 2,
                "visible": False
            },

        ]
    ]

    assert day_8_1.assign_visible_linearly(forest) == expected_forest
