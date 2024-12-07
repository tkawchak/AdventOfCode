# Regex: (mul\([0-9]*,[0-9]*\))

import re

TEST_STRING = (
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
)

# Regex for finding inactive parts of the string
bad = re.compile(r"don't\(\)")
good = re.compile(r"do\(\)")

p = re.compile(r"mul\(([0-9]*),([0-9]*)\)")


def find_matches(input_text: str):
    current_text = input_text
    bad_match = bad.search(current_text)
    good_match = good.search(current_text)

    valid_matches = []
    while bad_match is not None:
        matches = p.findall(current_text[: bad_match.start()])
        print(matches)
        valid_matches += matches

        current_text = current_text[bad_match.end() :]
        good_match = good.search(current_text)
        if good_match is None:
            break
        current_text = current_text[good_match.end() :]
        bad_match = bad.search(current_text)

    matches = p.findall(current_text)
    print(matches)
    valid_matches += matches

    print(sum([int(x) * int(y) for x, y in valid_matches]))


with open("input.txt") as f:
    input_text = f.read()
    find_matches(input_text)
