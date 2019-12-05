from PuzzleInput import ReadInput

pz_input = ReadInput(16).data


def part_a():
    known = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}
    for aunt in pz_input:
        pieces = aunt.split(" ")
        valid = True
        for i in range(2, len(pieces), 2):
            value = pieces[i+1]
            if value[-1] == ",":
                value = value[:-1]
            if known[pieces[i][:-1]] != int(value):
                valid = False
                break
        if valid:
            return int(pieces[1][:-1])
    floor = 0
    return floor


def part_b():
    known = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5,
             "trees": 3, "cars": 2, "perfumes": 1}
    for aunt in pz_input:
        pieces = aunt.split(" ")
        valid = True
        for i in range(2, len(pieces), 2):
            value = pieces[i + 1]
            if value[-1] == ",":
                value = value[:-1]
            if pieces[i][:-1] in ["cats", "trees"] and known[pieces[i][:-1]] >= int(value):
                valid = False
                break
            elif pieces[i][:-1] in ["pomeranians", "goldfish"] and known[pieces[i][:-1]] <= int(value):
                valid = False
                break
            elif pieces[i][:-1] not in ["pomeranians", "goldfish", "cats", "trees"] and known[pieces[i][:-1]] != int(value):
                valid = False
                break
        if valid:
            return int(pieces[1][:-1])
    floor = 0
    return floor


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
