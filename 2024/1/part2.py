from parse_list import parse_lists
from collections import defaultdict

FILENAME: str = "test.txt"
SPLIT_CHAR: str = " "

# Read the file into 2 separate lists
list1, list2 = parse_lists(FILENAME)

# Count the number of times each element appears in the second list.
count_dict = defaultdict(int)
for item in list2:
    count_dict[item] += 1

# Find the sum of the product of each element in the first list by the count of it in the second list
print(sum([num * count_dict[num] for num in list1]))
