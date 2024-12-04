from typing import List

SPLIT_CHAR: str = " "


def parse_lists(filename: str) -> tuple[List[int], List[int]]:
    # Read the file into 2 separate lists
    list1: List[str] = []
    list2: List[str] = []
    with open(filename) as file:
        for line in file:
            line_array: List[str] = line.strip().split("   ")
            if len(line_array) == 0:
                continue
            list1.append(int(line_array[0]))
            list2.append(int(line_array[1]))

    return list1, list2
