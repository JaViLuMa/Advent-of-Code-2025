def rotate_dial(direction, value_to_rotate, current_dial_value):
    pointed_or_seen_zero = 0
    new_dial_value = current_dial_value

    if direction == "L":
        starting_value = 100 if current_dial_value == 0 else current_dial_value

        new_dial_value = starting_value - value_to_rotate

        pointed_or_seen_zero = (new_dial_value - 1) // 100
    else:
        new_dial_value = current_dial_value + value_to_rotate

        pointed_or_seen_zero = new_dial_value // 100

    return new_dial_value % 100, abs(pointed_or_seen_zero)


seen_zeroes = 0
pointed_at_zero = 0
current_dial_value = 50

with open("./input.txt") as f:
    for dial_instruction in f:
        dial_direction, rotation_value = dial_instruction[0], dial_instruction[1:]

        current_dial_value, pointed_or_seen_zero = rotate_dial(
            dial_direction, int(rotation_value), current_dial_value
        )

        pointed_at_zero += pointed_or_seen_zero

        if current_dial_value == 0:
            seen_zeroes += 1


print(f"Part 1: {seen_zeroes}")
print(f"Part 2: {pointed_at_zero}")
