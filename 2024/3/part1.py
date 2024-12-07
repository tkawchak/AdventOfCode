# Regex: (mul\([0-9]*,[0-9]*\))

import re

TEST_STRING = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
# m = re.match(r"mul\(([0-9]*),([0-9]*)\)", TEST_STRING)

p = re.compile(r"mul\(([0-9]*),([0-9]*)\)")
with open("input.txt") as f:
    text_to_parse = f.read()
    print(sum([int(x) * int(y) for x, y in p.findall(text_to_parse)]))
