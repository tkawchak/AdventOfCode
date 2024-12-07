def is_safe(report):
    increasing = all(
        1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1)
    )
    decreasing = all(
        1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1)
    )
    return increasing or decreasing


def can_be_safe_with_dampener(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1 :]
        if is_safe(modified_report):
            return True
    return False


def count_safe_reports(reports):
    safe_count = 0
    for report in reports:
        safe: bool = is_safe(report) or can_be_safe_with_dampener(report)
        print(f"{','.join(map(str, report))}\t{safe}")
        safe_count += 1 if safe else 0
    return safe_count


# Read the reports from test.txt
with open("input.txt") as f:
    reports = [list(map(int, line.split())) for line in f]

# Count the safe reports
safe_reports_count = count_safe_reports(reports)
print(f"Number of safe reports: {safe_reports_count}")
