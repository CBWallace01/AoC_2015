from PuzzleInput import ReadInput

pz_input = ["c", "q", "j", "x", "j", "n", "d", "s"]


def is_valid(passwd):
    # ord(a) = 97, z = chr(122)
    contains_sequence = (ord(passwd[0]) + 2 == ord(passwd[1]) + 1 == ord(passwd[2])) or \
                        (ord(passwd[1]) + 2 == ord(passwd[2]) + 1 == ord(passwd[3])) or \
                        (ord(passwd[2]) + 2 == ord(passwd[3]) + 1 == ord(passwd[4])) or \
                        (ord(passwd[3]) + 2 == ord(passwd[4]) + 1 == ord(passwd[5])) or \
                        (ord(passwd[4]) + 2 == ord(passwd[5]) + 1 == ord(passwd[6])) or \
                        (ord(passwd[5]) + 2 == ord(passwd[6]) + 1 == ord(passwd[7]))
    contains_invalid = "i" in passwd or "o" in passwd or "l" in passwd
    contains_pairs = False
    for i in range(6):
        if passwd[i] == passwd[i+1]:
            for j in range(i+2, 7):
                if passwd[j] == passwd[j+1]:
                    contains_pairs = True
    return contains_sequence and contains_pairs and not contains_invalid


def part_a():
    current = pz_input
    while not is_valid(current):
        for i in range(7, -1, -1):
            current[i] = chr(ord(current[i]) + 1)
            if ord(current[i]) <= 122:
                break
            else:
                current[i] = "a"
    return current


def part_b():
    current = ["c", "q", "j", "x", "x", "z", "a", "a"]
    while not is_valid(current):
        for i in range(7, -1, -1):
            current[i] = chr(ord(current[i]) + 1)
            if ord(current[i]) <= 122:
                break
            else:
                current[i] = "a"
    return current


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
