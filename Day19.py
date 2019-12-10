from PuzzleInput import ReadInput
import re

pz_input = [x for x in ReadInput(19).data if len(x) > 0]


def part_a():
    conversions = [x.split(" => ") for x in pz_input[:-1]]
    molecule = pz_input[-1]
    results = []
    for conv in conversions:
        found = re.search(conv[0], molecule)
        offset = 0
        while found is not None:
            loc = found.span()
            loc = (loc[0] + offset, loc[1] + offset)
            new_molecule = molecule[:loc[0]] + conv[1] + molecule[loc[1]:]
            if new_molecule not in results:
                results.append(new_molecule)
            found = re.search(conv[0], molecule[loc[1]:])
            offset += loc[1]
    return len(results)


def part_b():
    pass


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
