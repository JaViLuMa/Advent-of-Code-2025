def part_1(id):
    if len(id) % 2 != 0:
        return 0

    id_set = set(list(id))

    if len(id_set) == 1:
        return id

    middle_index = len(id) // 2

    if id[:middle_index] == id[middle_index:]:
        return id

    return 0


def repeating_substring(id):
    for i in range(1, len(id) // 2 + 1):
        if len(id) % i != 0:
            continue

        current_substring = id[:i]

        if current_substring * (len(id) // i) == id:
            return id.count(current_substring)

    return 0


def part_2(id):
    id_set = set(list(id))

    if len(id_set) == 1 and len(id) >= 2:
        return id

    count_of_repeats = repeating_substring(id)

    if count_of_repeats >= 2:
        return id

    return 0


id_ranges_line = open("./input.txt").readline()

id_ranges = id_ranges_line.split(",")

part_1_sum = 0
part_2_sum = 0

for id_range in id_ranges:
    start, end = list(map(int, id_range.split("-")))

    for id in range(start, end + 1):
        id_as_string = str(id)

        part_1_sum += int(part_1(id_as_string))
        part_2_sum += int(part_2(id_as_string))

print(f"Part 1: {part_1_sum}")
print(f"Part 2: {part_2_sum}")
