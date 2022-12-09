from typing import TypedDict


def extract_forest():
    file = open("input.txt")
    return file.readlines()


class Tree(TypedDict):
    height: int
    visible: bool


Forest = list[list[Tree]]


def transform_forest(raw_forest: list[str]) -> Forest:
    forest: Forest = []
    for raw_row in raw_forest:
        row: list[Tree] = []
        for raw_tree_height in raw_row:
            if raw_tree_height == '\n':
                continue
            tree: Tree = {
                "height": int(raw_tree_height),
                "visible": False
            }
            row.append(tree)
        forest.append(row)
    return forest


def assign_visible_linearly(forest: Forest) -> Forest:
    assigned_forest: Forest = []
    for row in forest:
        assigned_row: list[Tree] = []
        first_tree: Tree = {
            "height": row[0]["height"],
            "visible": True
        }
        highest_tree = first_tree["height"]
        assigned_row.append(first_tree)

        for tree in row[1:]:
            if tree["height"] > highest_tree:
                highest_tree = tree["height"]
                tree["visible"] = True
            assigned_row.append(tree)
        assigned_forest.append(assigned_row)

    return assigned_forest


def rotate_forest_90_degrees(forest: Forest) -> Forest:
    rotated_forest = list(zip(*forest))[::-1]
    return [list(x) for x in rotated_forest]


def main():
    raw_forest = extract_forest()
    forest = transform_forest(raw_forest)
    for _ in range(4):
        forest = assign_visible_linearly(forest)
        forest = rotate_forest_90_degrees(forest)
    visible: list[Tree] = []
    for row in forest:
        visible += [x for x in row if x["visible"]]
    print(len(visible))


main()
