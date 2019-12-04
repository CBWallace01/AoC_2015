from PuzzleInput import ReadInput

pz_input = ReadInput(5).data


def part_a():
    nice = 0
    for kid in pz_input:
        vowels = len([letter for letter in kid if letter in ["a", "e", "i", "o", "u"]])
        double = False
        for i in range(len(kid)-1):
            if kid[i] == kid[i+1]:
                double = True
                break
        forbidden = False
        for i in range(len(kid)-1):
            if kid[i:i+2] in ["ab", "cd", "pq", "xy"]:
                forbidden = True
                break
        if vowels >= 3 and double and not forbidden:
            nice += 1
    return nice


def part_b():
    nice = 0
    for kid in pz_input:
        repeat = False
        for i in range(len(kid)-2):
            if kid[i:i+2] in kid[i+2:]:
                repeat = True
                break
        sandwich = False
        for i in range(len(kid)-2):
            if kid[i] == kid[i+2]:
                sandwich = True
                break
        if repeat and sandwich:
            nice += 1
    return nice


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
