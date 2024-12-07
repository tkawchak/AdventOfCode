from typing import List

MAX_CHANGE: int = 3
MIN_CHANGE: int = 1


def is_safe(levels: List[str]) -> bool:
    if len(levels) < 2:
        return True

    safe: bool = True
    prev: int = int(levels[0])
    increasing: bool = int(levels[0]) < int(levels[1])
    for num in levels[1:]:
        if increasing and (
            int(num) - prev > MAX_CHANGE or int(num) - prev < MIN_CHANGE
        ):
            safe = False
            break
        elif not increasing and (
            prev - int(num) > MAX_CHANGE or prev - int(num) < MIN_CHANGE
        ):
            safe = False
            break
        prev = int(num)

    return safe
