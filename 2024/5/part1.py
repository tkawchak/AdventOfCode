from typing import List, Tuple, Set
from collections import defaultdict

FILENAME = "input.txt"


def read_file(file_name: str) -> Tuple[List[Tuple[int, int]], List[List[int]]]:
    rules: List[Tuple[int, int]] = []
    pages: List[List[int]] = []

    with open(file_name, "r") as file:
        line = file.readline().strip()
        while line != "":
            rules.append(tuple(map(int, line.split("|"))))
            line = file.readline().strip()

        line = file.readline().strip()
        while line != "":
            pages.append(list(map(int, line.split(","))))
            line = file.readline().strip()

    return rules, pages


rules, pages = read_file(FILENAME)

rule_map: defaultdict[int, List[int]] = defaultdict(list)
for rule in rules:
    rule_map[rule[1]].append(rule[0])

valid_pages: List[List[int]] = []
for page in pages:
    page_prev: Set[int] = set()
    page_all: Set[int] = set(page)
    valid = True
    for num in page:
        for prev in rule_map[num]:
            if prev not in page_prev and prev in page_all:
                valid = False
                break
        page_prev.add(num)

    if valid:
        valid_pages.append(page)

middle_nums = [page[len(page) // 2] for page in valid_pages]
print(sum(middle_nums))
