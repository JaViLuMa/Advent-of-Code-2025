from functools import lru_cache


def get_starting_position(tachyon_manifold):
    row = 0
    column = len(tachyon_manifold[row]) // 2

    return (row, column)


def part_1(tachyon_manifold, positions, total_splits=0):
    if len(positions) == 0:
        return total_splits

    current_splits = total_splits
    new_positions = set()

    for position in positions:
        position_row, position_column = position

        if position_row == len(tachyon_manifold) - 1:
            return total_splits

        new_position_row = position_row + 1

        if tachyon_manifold[new_position_row][position_column] == "^":
            new_positions.add((new_position_row, position_column - 1))
            new_positions.add((new_position_row, position_column + 1))
            current_splits += 1
        else:
            new_positions.add((new_position_row, position_column))

    return part_1(tachyon_manifold, new_positions, current_splits)


@lru_cache
def get_all_timelines(tachyon_manifold, position):
    current_position_row, current_position_column = position

    if current_position_row == len(tachyon_manifold) - 1:
        return 1

    new_position_row = current_position_row + 1

    if new_position_row >= len(tachyon_manifold):
        return 0

    possible_timelines = 0

    if tachyon_manifold[new_position_row][current_position_column] == "^":
        possible_timelines += get_all_timelines(
            tachyon_manifold, (new_position_row, current_position_column - 1)
        )
        possible_timelines += get_all_timelines(
            tachyon_manifold, (new_position_row, current_position_column + 1)
        )
    else:
        possible_timelines += get_all_timelines(
            tachyon_manifold, (new_position_row, current_position_column)
        )

    return possible_timelines


def part_2(tachyon_manifold, position):
    tachyon_manifold_as_tuple = tuple(tuple(row) for row in tachyon_manifold)

    return get_all_timelines(tachyon_manifold_as_tuple, position)


tachyon_manifold = []

with open("./input.txt") as f:
    for line in f:
        tachyon_manifold.append(list(line.strip()))

starting_position = get_starting_position(tachyon_manifold)

total_splits = part_1(tachyon_manifold, {starting_position})
total_timelines = part_2(tachyon_manifold, starting_position)

print(f"Part 1: {total_splits}")
print(f"Part 2: {total_timelines}")
