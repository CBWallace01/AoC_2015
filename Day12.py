from PuzzleInput import ReadInput
import json

pz_input = ReadInput(12).data[0]


def value_of_collection(collection):
    total = 0
    if isinstance(collection, dict):
        if "red" in collection.keys() or "red" in collection.values():
            return 0
    for item in collection:
        if isinstance(item, int):
            total += item
        elif isinstance(collection, dict) and isinstance(collection[item], int):
            total += collection[item]
        elif isinstance(collection, dict) and (isinstance(collection[item], dict) or isinstance(collection[item], list)):
            total += value_of_collection(collection[item])
        elif isinstance(collection, list) and (isinstance(item, dict) or isinstance(item, list)):
            total += value_of_collection(item)
    return total


def part_a():
    pz_json = json.loads(pz_input)
    total = 0
    elements = []
    for item in pz_json:
        if isinstance(item, int):
            total += item
        else:
            elements.append(pz_json[item])
    while len(elements) > 0:
        next_chunk = elements.pop()
        if isinstance(next_chunk, int):
            total += next_chunk
        elif isinstance(next_chunk, dict):
            for item in next_chunk:
                elements.append(next_chunk[item])
        elif isinstance(next_chunk, list):
            for item in next_chunk:
                if isinstance(item, int):
                    total += item
                else:
                    elements.append(item)
    return total


def part_b():
    pz_json = json.loads(pz_input)
    return value_of_collection(pz_json)


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
