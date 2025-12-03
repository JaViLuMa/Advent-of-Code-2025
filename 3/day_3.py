def calculate_joltage(battery, length):
    if length == 0:
        return ""

    safe_search_zone = len(battery) - length + 1

    next_digit = max(battery[:safe_search_zone])

    next_digit_position = battery.find(next_digit)

    return next_digit + calculate_joltage(
        battery[next_digit_position + 1 :], length - 1
    )


joltage_sum_part_1 = 0
joltage_sum_part_2 = 0

with open("./input.txt") as f:
    for battery in f:
        battery = battery.strip()

        joltage_sum_part_1 += int(calculate_joltage(battery, 2))
        joltage_sum_part_2 += int(calculate_joltage(battery, 12))

print(f"Part 1: {joltage_sum_part_1}")
print(f"Part 2: {joltage_sum_part_2}")
