from safe import is_safe

FILENAME: str = "input.txt"
MAX_CHANGE: int = 3
MIN_CHANGE: int = 1
MAX_SKIPS: int = 1

safe_count: int = 0
for line in open(FILENAME):
    levels = line.strip().split(" ")

    if len(levels) < 2:
        safe_count += 1
        continue

    safe: bool = True
    prev: int = int(levels[0])
    increasing: bool = int(levels[0]) < int(levels[1])
    skip_count: int = 0
    for idx, num in enumerate(levels[1:]):
        if increasing and (
            int(num) - prev > MAX_CHANGE or int(num) - prev < MIN_CHANGE
        ):
            safe = False
        elif not increasing and (
            prev - int(num) > MAX_CHANGE or prev - int(num) < MIN_CHANGE
        ):
            safe = False
        else:
            prev = int(num)
            continue

        if skip_count < MAX_SKIPS:
            skip_count += 1
            if idx == 0:
                increasing = int(levels[0]) < int(levels[2])
            safe = True
            continue  # skip the prev update if not safe
        else:
            break

    # Check the case where we start with a number to skip
    if not safe:
        safe = is_safe(levels[1:])
    if not safe:
        levels.remove(levels[1])
        safe = is_safe(levels)

    safe_count += 1 if safe else 0
    print(f"{','.join(levels)}\t{safe}")

print(safe_count)
