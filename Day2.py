from PuzzleInput import ReadInput

pz_input = ReadInput(2).data


def part_a():
    total = 0
    for box in pz_input:
        sides = box.split("x")
        if len(sides) < 3:
            continue
        for i in range(3):
            sides[i] = int(sides[i])
        total += (2 * sides[0] * sides[1]) + (2 * sides[1] * sides[2]) + (2 * sides[0] * sides[2]) + min(sides[0]*sides[1], min(sides[1]*sides[2], sides[0]*sides[2]))
    return total


def part_b():
    total = 0
    for box in pz_input:
        sides = box.split("x")
        if len(sides) < 3:
            continue
        for i in range(3):
            sides[i] = int(sides[i])
        min_1 = min(sides[0], sides[1])
        min_2 = min(sides[2], max(sides[0], sides[1]))
        total += (min_1 * 2) + (min_2 * 2) + (sides[0] * sides[1] * sides[2])
    return total


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
