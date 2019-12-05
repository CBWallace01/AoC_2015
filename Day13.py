from PuzzleInput import ReadInput
from collections import defaultdict

pz_input = ReadInput(13).data


def part_a():
    modifiers = defaultdict(lambda: {})
    for case in pz_input:
        if case == "":
            continue
        pieces = case.split(" ")
        modifiers[pieces[0]][pieces[10][:-1]] = int(pieces[3]) * (1 if pieces[2] == "gain" else -1)
    permutations = []
    current_perm = ["Alice"]
    while len(current_perm) < len(modifiers):
        for person in modifiers:
            if person not in current_perm:
                new_perm = current_perm.copy()
                new_perm.append(person)
                permutations.append(new_perm)
        current_perm = permutations.pop(0)
    change = []
    for perm in permutations:
        val = 0
        for i in range(len(perm)):
            val += modifiers[perm[i]][perm[(i + 1) % len(modifiers)]]
            val += modifiers[perm[i]][perm[(i - 1) % len(modifiers)]]
        change.append(val)
    return max(change)


def part_b():
    modifiers = defaultdict(lambda: {})
    for case in pz_input:
        if case == "":
            continue
        pieces = case.split(" ")
        modifiers[pieces[0]][pieces[10][:-1]] = int(pieces[3]) * (1 if pieces[2] == "gain" else -1)
    for k in [x for x in modifiers]:
        modifiers[k]["Me"] = 0
        modifiers["Me"][k] = 0
    permutations = []
    current_perm = ["Alice"]
    while len(current_perm) < len(modifiers):
        for person in modifiers:
            if person not in current_perm:
                new_perm = current_perm.copy()
                new_perm.append(person)
                permutations.append(new_perm)
        current_perm = permutations.pop(0)
    change = []
    for perm in permutations:
        val = 0
        for i in range(len(perm)):
            val += modifiers[perm[i]][perm[(i + 1) % len(modifiers)]]
            val += modifiers[perm[i]][perm[(i - 1) % len(modifiers)]]
        change.append(val)
    return max(change)


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
