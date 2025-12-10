from collections import deque
from z3 import Optimize, Int, Sum, sat


def bfs(target_light_diagram, buttons):
    target = tuple(target_light_diagram)

    length_of_target = len(target_light_diagram)

    current_diagram = tuple(False for _ in range(length_of_target))

    visited = {current_diagram: 0}

    queue = deque([current_diagram])

    while queue:
        current_diagram = queue.popleft()

        how_many_times = visited[current_diagram] + 1

        for button in buttons:
            next_current = tuple(
                not current_diagram[i] if i in button else current_diagram[i]
                for i in range(length_of_target)
            )

            if next_current not in visited:
                if next_current == target:
                    return how_many_times

                visited[next_current] = how_many_times

                queue.append(next_current)

    return 0


def get_min_button_presses_for_target_joltage(buttons, joltage):
    optimizer = Optimize()

    press_count = []

    for i in range(len(buttons)):
        variable = Int(f"b_{i}")

        optimizer.add(variable >= 0)

        press_count.append(variable)

    target_len = len(joltage)

    for j in range(target_len):
        contributors = []

        for i, button in enumerate(buttons):
            if j in button:
                contributors.append(press_count[i])

        if contributors:
            optimizer.add(Sum(contributors) == joltage[j])
        else:
            if joltage[j] > 0:
                return 0

    total_presses = Sum(press_count)

    optimizer.minimize(total_presses)

    if optimizer.check() == sat:
        model = optimizer.model()

        return model.eval(total_presses).as_long()
    else:
        return 0


normalized_input = []

with open("./input.txt") as f:
    for line in f:
        split_line = line.strip().split()

        target_light_diagram = list(light == "#" for light in split_line[0][1:-1])

        buttons = [
            list(map(int, button[1:-1].split(","))) for button in split_line[1:-1]
        ]

        joltage = list(map(int, split_line[-1][1:-1].split(",")))

        normalized_input.append((target_light_diagram, buttons, joltage))


fewest_presses_light_sum = sum(
    bfs(target, buttons) for target, buttons, _ in normalized_input
)

fewest_presses_joltage_sum = sum(
    get_min_button_presses_for_target_joltage(buttons, joltage)
    for _, buttons, joltage in normalized_input
)

print(f"Part 1: {fewest_presses_light_sum}")
print(f"Part 2: {fewest_presses_joltage_sum}")
