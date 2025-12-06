def transpose(problems):
    return list(zip(*problems))


def part_1(worksheet):
    normalized_worksheet = [problem.strip().split() for problem in worksheet]

    total = 0

    for *nums, op in transpose(normalized_worksheet):
        total += eval(op.join(nums))

    return total


def group_up(worksheet):
    groups = []
    current_group = []

    for problem in worksheet:
        if len(set(problem)) == 1:
            groups.append(current_group)
            current_group = []
        else:
            current_group.append(problem)

    groups.append(current_group)

    return groups


def part_2(worksheet):
    normalized_worksheet = transpose(worksheet)

    grouped_up_problems = group_up(normalized_worksheet)

    total = 0

    for group in grouped_up_problems:
        op = group[0][-1]

        all_nums_grouped = ["".join(nums) for *nums, _ in group]

        total += eval(op.join(all_nums_grouped))

    return total


worksheet = []

with open("./input.txt") as f:
    for line in f:
        worksheet.append(line.strip("\n"))

total_1 = part_1(worksheet)
total_2 = part_2(worksheet)

print(f"Part 1: {total_1}")
print(f"Part 2: {total_2}")
