from PuzzleInput import ReadInput

pz_input = ReadInput(3).data[0]


def part_a():
    visited = [(0, 0)]
    x = 0
    y = 0
    for move in pz_input:
        if move == "^":
            y += 1
        elif move == "v":
            y -= 1
        elif move == ">":
            x += 1
        elif move == "<":
            x -= 1
        else:
            raise IndexError(move)
        if (x, y) not in visited:
            visited.append((x, y))
    return len(visited)


def part_b():
    visited = [(0, 0)]
    loc = [0, 0, 0, 0]
    santa = True
    for move in pz_input:
        if move == "^":
            loc[1 + (0 if santa else 2)] += 1
        elif move == "v":
            loc[1 + (0 if santa else 2)] -= 1
        elif move == ">":
            loc[0 + (0 if santa else 2)] += 1
        elif move == "<":
            loc[0 + (0 if santa else 2)] -= 1
        else:
            raise IndexError(move)
        if (loc[0 + (0 if santa else 2)], loc[1 + (0 if santa else 2)]) not in visited:
            visited.append((loc[0 + (0 if santa else 2)], loc[1 + (0 if santa else 2)]))
        santa = not santa
    return len(visited)


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())

