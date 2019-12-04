from PuzzleInput import ReadInput

pz_input = ReadInput(1).data[0]


def part_a():
    floor = 0
    for char in pz_input:
        if char == ")":
            floor -= 1
        elif char == "(":
            floor += 1
    return floor


def part_b():
    floor = 0
    for i in range(len(pz_input)):
        if pz_input[i] == ")":
            floor -= 1
        elif pz_input[i] == "(":
            floor += 1
        if floor == -1:
            return i+1
    return floor


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
