from PuzzleInput import ReadInput
import re

pz_input = [x for x in ReadInput(19).data if len(x) > 0]


def try_replace(string, conversions):
    conversions.sort(key=lambda c: len(c[0]), reverse=True)
    for conv in conversions:
        all_matches = [(x.start(0), x.end(0)) for x in re.finditer(conv[0], string)]
        if len(all_matches) == 0:
            continue
        for match in all_matches:
            new_molecule = string[:match[0]] + conv[1] + string[match[1]:]
            if new_molecule == "e":
                return 0
            else:
                result = try_replace(new_molecule, conversions)
                if result >= 0:
                    return result + 1
    return -1


def part_a():
    conversions = [x.split(" => ") for x in pz_input[:-1]]
    molecule = pz_input[-1]
    results = []
    for conv in conversions:
        all_matches = [(x.start(0), x.end(0)) for x in re.finditer(conv[0], molecule)]
        for match in all_matches:
            new_molecule = molecule[:match[0]] + conv[1] + molecule[match[1]:]
            if new_molecule not in results:
                results.append(new_molecule)
    return len(results)


def part_b():
    conversions = [[x[1], x[0]] for x in [x.split(" => ") for x in pz_input[:-1]]]
    conversions = [[x[1], x[0]] for x in [["e", "H"], ["e", "O"], ["H", "HO"], ["H", "OH"], ["O", "HH"]]]
    molecule = pz_input[-1]
    molecule = "HOHOHO"
    return try_replace(molecule, conversions) + 1


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
