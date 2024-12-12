from typing import List, Optional, Tuple

FILENAME: str = "input.txt"


def read_file(file_name: str) -> List[List[str]]:
    with open(file_name, "r") as f:
        return [[x for x in line.strip()] for line in f]


COUNT: int = 0


def is_mas(a: str, b: str) -> bool:
    return (a == "M" and b == "S") or (a == "S" and b == "M")


def top_level_search(map: List[List[str]], start: Tuple[int, int]) -> None:
    global COUNT
    if is_mas(
        map[start[0] - 1][start[1] - 1], map[start[0] + 1][start[1] + 1]
    ) and is_mas(map[start[0] - 1][start[1] + 1], map[start[0] + 1][start[1] - 1]):
        COUNT += 1


word_lists = read_file(FILENAME)

for i in range(1, len(word_lists) - 1):
    for j in range(1, len(word_lists[i]) - 1):
        if word_lists[i][j] == "A":
            top_level_search(word_lists, (i, j))

print(COUNT)
