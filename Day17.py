from PuzzleInput import ReadInput

pz_input = [int(x) for x in ReadInput(17).data[:-2]]


def part_a():
    init_combo = []
    for i in range(len(pz_input)):
        init_combo.append([i])
    for i in range(1, len(pz_input)):
        curr_combos = [x for x in init_combo if len(x) == i]
        print("Creating size %s (%s to expand)" % (i + 1, len(curr_combos)))
        for combo in curr_combos:
            for j in range(len(pz_input)):
                if j not in combo:
                    new_combo = combo.copy()
                    new_combo.append(j)
                    new_combo.sort()
                    values = [pz_input[x] for x in new_combo]
                    if new_combo not in init_combo and sum(values) <= 150:
                        init_combo.append(new_combo)
    valid_total = 0
    for combo in init_combo:
        total = 0
        for x in combo:
            total += pz_input[x]
        if total == 150:
            valid_total += 1
    return valid_total


def part_b():
    init_combo = []
    for i in range(len(pz_input)):
        init_combo.append([i])
    found_valid = False
    for i in range(1, len(pz_input)):
        curr_combos = [x for x in init_combo if len(x) == i]
        print("Creating size %s (%s to expand)" % (i + 1, len(curr_combos)))
        for combo in curr_combos:
            for j in range(len(pz_input)):
                if j not in combo:
                    new_combo = combo.copy()
                    new_combo.append(j)
                    new_combo.sort()
                    values = [pz_input[x] for x in new_combo]
                    if new_combo not in init_combo and sum(values) <= 150:
                        init_combo.append(new_combo)
                        if sum(values) == 150:
                            found_valid = True
        if found_valid:
            break
    valid_total = 0
    for combo in init_combo:
        total = 0
        for x in combo:
            total += pz_input[x]
        if total == 150:
            valid_total += 1
    return valid_total


if __name__ == "__main__":
    # print("Part A", part_a())
    print("Part B", part_b())
