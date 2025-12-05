def check_if_fresh(ingredient, ingredient_range):
    start, end = list(map(int, ingredient_range.split("-")))

    if start <= int(ingredient) <= end:
        return True

    return False


def part_1(ingredients, ingredient_ranges):
    fresh_ingredients = 0

    for ingredient in ingredients:
        for ingredient_range in ingredient_ranges:
            is_fresh = check_if_fresh(ingredient, ingredient_range)

            if is_fresh:
                fresh_ingredients += 1

                break

    return fresh_ingredients


def get_range_boundaries(ingredient_ranges):
    range_boundaries = set()

    for ingredient_range in ingredient_ranges:
        start, end = list(map(int, ingredient_range.split("-")))

        range_boundaries.add(start)
        range_boundaries.add(end + 1)

    return sorted(list(range_boundaries))


def check_if_range_is_covered(range_boundaries, i, ingredient_ranges):
    start = range_boundaries[i]
    end = range_boundaries[i + 1]

    for ingredient_range in ingredient_ranges:
        is_fresh = check_if_fresh(start, ingredient_range)

        if is_fresh:
            return end - start

    return 0


def part_2(ingredient_ranges):
    all_possible_fresh_ingredients = 0

    range_boundaries = get_range_boundaries(ingredient_ranges)

    for i in range(len(range_boundaries) - 1):
        all_possible_fresh_ingredients += check_if_range_is_covered(
            range_boundaries, i, ingredient_ranges
        )

    return all_possible_fresh_ingredients


ingredient_ranges = []
ingredients = []

with open("./input.txt") as f:
    for ingredient_range in f:
        if ingredient_range == "\n":
            break

        ingredient_ranges.append(ingredient_range)

    for ingredient in f:
        ingredients.append(ingredient)

fresh_ingredients = part_1(ingredients, ingredient_ranges)
all_possible_fresh_ingredients = part_2(ingredient_ranges)

print(f"Part 1: {fresh_ingredients}")
print(f"Part 2: {all_possible_fresh_ingredients}")
