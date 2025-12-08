import sys
import math
from itertools import combinations


sys.setrecursionlimit(10**6)


def euclidean_distance(first_junction_box, second_junction_box):
    x1, y1, z1 = first_junction_box
    x2, y2, z2 = second_junction_box

    x = pow(x2 - x1, 2)
    y = pow(y2 - y1, 2)
    z = pow(z2 - z1, 2)

    return math.sqrt(x + y + z)


def generate_box_pairs(junction_boxes):
    circuits = {junction_box: {junction_box} for junction_box in junction_boxes}

    pairs_of_circuits = combinations(circuits, 2)

    sort_pairs = sorted(pairs_of_circuits, key=lambda x: euclidean_distance(x[0], x[1]))

    return circuits, sort_pairs


def process_circuits(circuits, pairs, current_iteration, part_2=False):
    box_1, box_2 = pairs[current_iteration]
    circuit_1, circuit_2 = None, None

    for circuit in circuits:
        if box_1 in circuits[circuit]:
            circuit_1 = circuit
        if box_2 in circuits[circuit]:
            circuit_2 = circuit

    if circuit_1 != circuit_2:
        circuits[circuit_1].update(circuits[circuit_2])

        del circuits[circuit_2]

    if current_iteration + 1 == 1000 and not part_2:
        sorted_circuits = sorted(len(circuits[circuit]) for circuit in circuits)

        return sorted_circuits[-3] * sorted_circuits[-2] * sorted_circuits[-1]

    if len(circuits) == 1 and part_2:
        return box_1[0] * box_2[0]

    return process_circuits(circuits, pairs, current_iteration + 1, part_2)


junction_boxes = []

with open("./input.txt") as f:
    for junction_box in f:
        normalize_junction_box = map(int, junction_box.strip().split(","))

        junction_boxes.append(tuple(normalize_junction_box))


circuits, circuit_pairs = generate_box_pairs(junction_boxes)

mul_of_three_largest_circuits = process_circuits(circuits, circuit_pairs, 0)
mul_of_x_coordinates = process_circuits(circuits, circuit_pairs, 0, True)

print(f"Part 1: {mul_of_three_largest_circuits}")
print(f"Part 2: {mul_of_x_coordinates}")
