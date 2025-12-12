def check_if_gifts_fit(shapes, regions):
    fitting_regions = 0

    for region in regions:
        size = region["size"]
        amounts = region["amounts"]

        area_of_region = size[0] * size[1]

        total_shapes_area = 0

        for i, amount in enumerate(amounts):
            shape = shapes[i]

            shape_area = sum(part_of_shape.count("#") for part_of_shape in shape)

            total_shapes_area += shape_area * amount

        if area_of_region >= total_shapes_area:
            fitting_regions += 1

    return fitting_regions


shapes = {}
regions = []

with open("./input.txt") as f:
    current_id = None
    buffer = []

    for line in f:
        stripped_line = line.strip()

        if not stripped_line:
            continue

        if (
            "x" in stripped_line
            and ":" in stripped_line
            and not stripped_line.endswith(":")
        ):
            size, amounts = stripped_line.split(": ")

            regions.append(
                {
                    "size": list(map(int, size.split("x"))),
                    "amounts": list(map(int, amounts.split())),
                }
            )

            continue

        if stripped_line.endswith(":"):
            if current_id is not None:
                shapes[current_id] = buffer

            current_id = int(stripped_line[:-1])
            buffer = []
        else:
            buffer.append(stripped_line)

    if current_id is not None and buffer:
        shapes[current_id] = buffer


fitting_regions = check_if_gifts_fit(shapes, regions)

print(f"Part 1: {fitting_regions}")
print("Part 2: Merry Christmas :D")
