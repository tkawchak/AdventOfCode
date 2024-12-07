from safe import is_safe

FILENAME: str = "input.txt"

safe_count: int = 0
for line in open(FILENAME):
    levels = line.strip().split(" ")

    safe_count += 1 if is_safe(levels) else 0

print(safe_count)
