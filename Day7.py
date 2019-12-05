from PuzzleInput import ReadInput

pz_input = ReadInput(7).data


def part_a():
    rules = {}
    for rule in pz_input:
        if rule == "":
            continue
        pieces = rule.split(" -> ")
        logic = pieces[0].split(" ")
        if len(logic) == 1:
            rules[pieces[1]] = int(logic)
        elif len(logic) == 2:
            rules[pieces[1]] = (int(logic[1]), "NOT")
    test = [line for line in pz_input if line != "" and line.split(" -> ")[1] == "a"]

    floor = 0
    return floor


def part_b():
    floor = 0
    return floor


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
