from typing import TypedDict


def extract_forest():
    file = open("input.txt")
    return file.readlines()


class Tree(TypedDict):
    height: int
    score: int
    calculated: bool


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
                "score": 0,
                "calculated": False
            }
            row.append(tree)
        forest.append(row)
    return forest


def rotate_forest_90_degrees(forest: Forest) -> Forest:
    rotated_forest = list(zip(*forest))[::-1]
    return [list(x) for x in rotated_forest]


def calculate_visibility_scores(forest: Forest) -> Forest:
    calculated_forest: Forest = []
    for row in forest:
        calculated_row: list[Tree] = []
        for i in range(len(row)):
            if i == len(row)-1:
                row[i]["score"] = 0
                row[i]["calculated"] = True
                continue
            visibility = 1
            while row[i+visibility]["height"] < row[i]["height"] and i+visibility < len(row)-1:
                visibility += 1
            if row[i]["calculated"] == True:
                row[i]["score"] = row[i]["score"] * visibility
            else:
                row[i]["score"] = visibility
            row[i]["calculated"] = True
            calculated_row.append(row[i])
        calculated_forest.append(calculated_row)
    return calculated_forest


def main():
    raw_forest = extract_forest()
    forest = transform_forest(raw_forest)
    for _ in range(4):
        forest = calculate_visibility_scores(forest)
        forest = rotate_forest_90_degrees(forest)
    visibility_scores: list[int] = []
    for row in forest:
        visibility_scores += [x["score"] for x in row]
    print(max(visibility_scores))


main()
