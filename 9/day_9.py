from itertools import combinations


def get_compressed_coordinates(all_coordinates):
    all_columns = [col for col, _ in all_coordinates]
    all_rows = [row for _, row in all_coordinates]

    unique_columns = sorted(list(set(all_columns)))
    unique_rows = sorted(list(set(all_rows)))

    column_map = {val: i for i, val in enumerate(unique_columns)}
    row_map = {val: i for i, val in enumerate(unique_rows)}

    compressed = []

    for col, row in all_coordinates:
        new_col = column_map[col]
        new_row = row_map[row]

        compressed.append((new_col, new_row))

    return compressed, unique_columns, unique_rows


def calculate_area(pair, col_lookup, row_lookup):
    p1, p2 = pair

    p1_col, p1_row = p1
    p2_col, p2_row = p2

    col_1, row_1 = col_lookup[p1_col], row_lookup[p1_row]
    col_2, row_2 = col_lookup[p2_col], row_lookup[p2_row]

    return (abs((col_1 - col_2)) + 1) * (abs((row_1 - row_2)) + 1)


def get_largest_area(all_coordinates, col_lookup, row_lookup):
    pairs = combinations(all_coordinates, 2)

    largest_area = max(pairs, key=lambda x: calculate_area(x, col_lookup, row_lookup))

    return calculate_area(largest_area, col_lookup, row_lookup)


def is_point_inside_polygon(x, y, polygon_edges):
    intersections = 0

    for x_edge, y1, y2 in polygon_edges:
        if x_edge > x:
            if min(y1, y2) <= y <= max(y1, y2):
                intersections += 1

    return intersections % 2 == 1


def build_presence_grid(all_coordinates, col_lookup, row_lookup):
    edges = []

    num_points = len(all_coordinates)

    for i in range(num_points):
        pair_1 = all_coordinates[i]
        pair_2 = all_coordinates[(i + 1) % num_points]

        if pair_1[0] == pair_2[0]:
            edges.append((pair_1[0], pair_1[1], pair_2[1]))

    grid_width = len(col_lookup) - 1
    grid_height = len(row_lookup) - 1

    grid = [[0] * grid_height for _ in range(grid_width)]

    for col in range(grid_width):
        for row in range(grid_height):
            mid_x = (col_lookup[col] + col_lookup[col + 1]) / 2
            mid_y = (row_lookup[row] + row_lookup[row + 1]) / 2

            if is_point_inside_polygon(mid_x, mid_y, edges):
                grid[col][row] = 1

    return grid


def build_2d_prefix_sum(grid):
    width = len(grid)
    height = len(grid[0])

    p_sum = [[0] * (height + 1) for _ in range(width + 1)]

    for i in range(width):
        for j in range(height):
            p_sum[i + 1][j + 1] = (
                grid[i][j] + p_sum[i][j + 1] + p_sum[i + 1][j] - p_sum[i][j]
            )

    return p_sum


def get_sum_from_prefix(p_sum, col_1, row_1, col_2, row_2):
    col_min, col_max = min(col_1, col_2), max(col_1, col_2)
    row_min, row_max = min(row_1, row_2), max(row_1, row_2)

    return (
        p_sum[col_max][row_max]
        - p_sum[col_min][row_max]
        - p_sum[col_max][row_min]
        + p_sum[col_min][row_min]
    )


def get_largest_confined_area(
    all_coordinates, compressed_coordinates, col_lookup, row_lookup
):
    grid = build_presence_grid(all_coordinates, col_lookup, row_lookup)

    p_sum = build_2d_prefix_sum(grid)

    pairs = combinations(compressed_coordinates, 2)

    max_area = 0

    for pair in pairs:
        col_1, row_1 = pair[0]
        col_2, row_2 = pair[1]

        if col_1 == col_2 or row_1 == row_2:
            continue

        col_min, col_max = min(col_1, col_2), max(col_1, col_2)
        row_min, row_max = min(row_1, row_2), max(row_1, row_2)

        expected_sum = (col_max - col_min) * (row_max - row_min)

        actual_sum = get_sum_from_prefix(p_sum, col_min, row_min, col_max, row_max)

        if actual_sum == expected_sum:
            area = calculate_area((pair[0], pair[1]), col_lookup, row_lookup)

            if area > max_area:
                max_area = area

    return max_area


all_coordinates = []

with open("./input.txt") as f:
    for line in f:
        coordinates = tuple(map(int, line.strip().split(",")))

        all_coordinates.append(coordinates)


compressed_coordinates, col_lookup, row_lookup = get_compressed_coordinates(
    all_coordinates
)

largest_area = get_largest_area(compressed_coordinates, col_lookup, row_lookup)
largest_confined_area = get_largest_confined_area(
    all_coordinates, compressed_coordinates, col_lookup, row_lookup
)

print(f"Part 1: {largest_area}")
print(f"Part 2: {largest_confined_area}")
