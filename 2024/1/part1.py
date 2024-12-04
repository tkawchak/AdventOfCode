from parse_list import parse_lists

FILENAME: str = "input.txt"

# Read the file into 2 separate lists
list1, list2 = parse_lists(FILENAME)

# Sort the lists so we can compare
list1.sort()
list2.sort()

# Find the absolute distances between each element in the lists and sum them
distance_array = [abs(item1 - item2) for (item1, item2) in zip(list1, list2)]
print(sum(distance_array))
