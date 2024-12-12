from typing import List, Optional, Tuple

FILENAME: str = "input.txt"


def read_file(file_name: str) -> List[List[str]]:
    with open(file_name, "r") as f:
        return [[x for x in line.strip()] for line in f]

def is_next(map: List[List[str]], start: Tuple[int, int], next_letter: str) -> bool:
    if start[0] < 0 or start[0] >= len(map):
        return False
    if start[1] < 0 or start[1] >= len(map[0]):
        return False
    return map[start[0]][start[1]] == next_letter

    
COUNT: int = 0
def search(map: List[List[str]], start: Tuple[int, int], current_letter: str, direction: Tuple[int, int]) -> None:
    global COUNT
    next_letter: str = ""
    match current_letter:
        case "X":
            next_letter = "M"
        case "M":
            next_letter = "A"
        case "A":
            next_letter = "S"
        case "S":
            COUNT += 1
            return
        case _:
            return

    if is_next(map, (start[0] + direction[0], start[1] + direction[1]), next_letter):
        search(map, (start[0] + direction[0], start[1] + direction[1]), next_letter, direction)
    
    return

def top_level_search(map: List[List[str]], start: Tuple[int, int], current_letter: str) -> None:
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            search(map, start, current_letter, (i, j))

word_lists = read_file(FILENAME)

for i in range(0, len(word_lists)):
    for j in range(0, len(word_lists[i])):
        if (word_lists[i][j] == "X"):
            top_level_search(word_lists, (i, j), "X")
        
print(COUNT)
