from PuzzleInput import ReadInput

pz_input = ReadInput(8).data


def part_a():
    code_total = 0
    for line in pz_input:
        i = 0
        while i < len(line):
            if line[i] == "\"":
                code_total += 1
                i += 1
            elif line[i] == "\\":
                if line[i + 1] == "x":
                    code_total += 3
                    i += 4
                else:
                    code_total += 1
                    i += 2
            else:
                i += 1
    return code_total


def part_b():
    # pz_input = ["\"\"", "\"abc\"", "\"aaa\\\"aaa\"", "\"\\x27\""]
    total = 0
    for line in pz_input:
        if line == "":
            continue
        total += 2  # For new surrounding quotes
        total += line.count("\"")
        total += line.count("\\")
    return total



if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
