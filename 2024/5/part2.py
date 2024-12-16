from typing import Dict, List, Tuple, Set
from collections import defaultdict

FILENAME = "input.txt"


def read_file(file_name: str) -> Tuple[List[Tuple[int, int]], List[List[int]]]:
    """
    Parse the file into the rule structure and list of pages
    """

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

# Find the invalid pages
invalid_pages: List[List[int]] = []
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

    if not valid:
        invalid_pages.append(page)

# Sort the invalid pages
for page in invalid_pages:
    page_prev: Set[int] = set()
    page_all: Dict[int, int] = {}
    for idx, num in enumerate(page):
        page_all[num] = idx
    i = 0
    while i < len(page):
        num = page[i]
        index = 0
        prev_num = 0

        # Find the max index of numbers that should be before the current number
        for prev in rule_map[num]:
            if prev in page_all and prev not in page_prev:
                index = max(index, page_all[prev])
                prev_num = prev

        # Perform the swap if needed
        if index > i:
            page.pop(i)
            page.insert(index, num)
            page_all[num] = index
            page_all[prev_num] = page_all[prev_num] - 1
        else:
            page_prev.add(num)
            i += 1

middle_nums = [page[len(page) // 2] for page in invalid_pages]
print(sum(middle_nums))
