import re


def parse_memory(memory):
    # Regular expressions to match the instructions
    mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
    do_pattern = re.compile(r"do\(\)")
    dont_pattern = re.compile(r"don\'t\(\)")

    # Initial state: mul instructions are enabled
    mul_enabled = True
    total_sum = 0

    # Scan through the memory
    pos = 0
    while pos < len(memory):
        # Check for mul instruction
        mul_match = mul_pattern.match(memory, pos)
        if mul_match:
            if mul_enabled:
                a, b = int(mul_match.group(1)), int(mul_match.group(2))
                total_sum += a * b
            pos = mul_match.end()
            continue

        # Check for do() instruction
        do_match = do_pattern.match(memory, pos)
        if do_match:
            mul_enabled = True
            pos = do_match.end()
            continue

        # Check for don't() instruction
        dont_match = dont_pattern.match(memory, pos)
        if dont_match:
            mul_enabled = False
            pos = dont_match.end()
            continue

        # Move to the next character if no instruction is found
        pos += 1

    return total_sum


# Read the input from input.txt
with open("input.txt") as f:
    memory = f.read().strip()

# Calculate the result
result = parse_memory(memory)
print(f"Sum of the results of just the enabled multiplications: {result}")
