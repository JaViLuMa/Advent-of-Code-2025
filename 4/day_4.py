adjacent_directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, 1),
    (-1, -1),
    (1, -1),
    (-1, 1),
]


def check_boundary(row, col, max_row, max_col):
    return 0 <= row < max_row and 0 <= col < max_col


def get_count_of_adjacent_rolls(warehouse, row, col):
    count = 0
    max_row = len(warehouse)
    max_col = len(warehouse[row])

    for direction in adjacent_directions:
        new_row = row + direction[0]
        new_col = col + direction[1]

        if not check_boundary(new_row, new_col, max_row, max_col):
            continue

        if warehouse[new_row][new_col] == "@":
            count += 1

    return count


def get_movable_roll_position(warehouse, current_row, current_column):
    if warehouse[current_row][current_column] != "@":
        return set()

    count_of_adjacent_rolls = get_count_of_adjacent_rolls(
        warehouse, current_row, current_column
    )

    if count_of_adjacent_rolls < 4:
        return {(current_row, current_column)}

    return set()


def get_total_movable_positions(warehouse):
    total_movable_positions = set()

    for row in range(len(warehouse)):
        for col in range(len(warehouse[row])):
            total_movable_positions.update(
                get_movable_roll_position(warehouse, row, col)
            )

    return total_movable_positions


def part_1(warehouse):
    movable_positions = get_total_movable_positions(warehouse)

    return len(movable_positions)


def part_2(warehouse):
    movable_positions = get_total_movable_positions(warehouse)

    if len(movable_positions) == 0:
        return 0

    for position in movable_positions:
        warehouse[position[0]][position[1]] = "."

    return len(movable_positions) + part_2(warehouse)


rolls_part_1 = 0
rolls_part_2 = 0

with open("./input.txt") as f:
    warehouse = [list(line.strip()) for line in f]

    rolls_part_1 += part_1(warehouse)
    rolls_part_2 += part_2(warehouse)

print(f"Part 1: {rolls_part_1}")
print(f"Part 2: {rolls_part_2}")
