from PuzzleInput import ReadInput

pz_input = "1113122113"


def part_a():
    current = pz_input
    for x in range(40):
        new_num = ""
        i = 0
        while i < len(current):
            value = current[i]
            count = 1
            j = 1
            while True:
                if i + j < len(current) and current[i + j] == value:
                    count += 1
                    j += 1
                else:
                    break
            new_num += str(count) + str(value)
            i += j
        current = new_num
    return len(current)


def part_b():
    current = pz_input
    for x in range(50):
        new_num = ""
        i = 0
        while i < len(current):
            value = current[i]
            count = 1
            j = 1
            while True:
                if i + j < len(current) and current[i + j] == value:
                    count += 1
                    j += 1
                else:
                    break
            new_num += str(count) + str(value)
            i += j
        current = new_num
    return len(current)


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
