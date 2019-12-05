from PuzzleInput import ReadInput

pz_input = ReadInput(7).data


def part_a():
    rules = {}
    for rule in pz_input:
        if rule == "":
            continue
        pieces = rule.split(" -> ")
        logic = pieces[0].split(" ")
        if len(logic) == 1:
            rules[pieces[1]] = [logic[0]]
        elif len(logic) == 2:
            rules[pieces[1]] = [logic[1], "NOT"]
        elif len(logic) == 3:
            rules[pieces[1]] = [logic[0], logic[1], logic[2]]
        else:
            raise ValueError("Invalid Length:", logic)
    while True:
        for k in rules:
            v = rules[k]
            if len(v) == 1:
                if isinstance(v[0], str) and v[0].isnumeric():
                    rules[k] = [int(v[0])]
                elif isinstance(v[0], str) and len(rules[v[0]]) == 1 and isinstance(rules[v[0]][0], int):
                    rules[k] = [rules[v[0]][0]]
            elif len(v) == 2:
                if len(rules[v[0]]) == 1 and isinstance(rules[v[0]][0], int) and v[1] == "NOT":
                    rules[k] = [~rules[v[0]][0]]
            elif len(v) == 3:
                for i in range(0, 3, 2):
                    v[i] = int(v[i]) if isinstance(v[i], str) and v[i].isnumeric() else v[i]
                if ((isinstance(v[0], str) and len(rules[v[0]]) == 1 and isinstance(rules[v[0]][0], int)) or isinstance(v[0], int)) and ((isinstance(v[2], str) and len(rules[v[2]]) == 1 and isinstance(rules[v[2]][0], int)) or isinstance(v[2], int)):
                    if v[1] == "AND":
                        left = (v[0] if isinstance(v[0], int) else rules[v[0]][0])
                        right = (v[2] if isinstance(v[2], int) else rules[v[2]][0])
                        rules[k] = [left & right]
                    elif v[1] == "OR":
                        left = (v[0] if isinstance(v[0], int) else rules[v[0]][0])
                        right = (v[2] if isinstance(v[2], int) else rules[v[2]][0])
                        rules[k] = [left | right]
                    elif v[1] == "RSHIFT":
                        left = (v[0] if isinstance(v[0], int) else rules[v[0]][0])
                        right = (v[2] if isinstance(v[2], int) else rules[v[2]][0])
                        rules[k] = [left >> right]
                    elif v[1] == "LSHIFT":
                        left = (v[0] if isinstance(v[0], int) else rules[v[0]][0])
                        right = (v[2] if isinstance(v[2], int) else rules[v[2]][0])
                        rules[k] = [left << right]
                    else:
                        raise ValueError("Unknown Command:", v[1])
            else:
                raise ValueError("Invalid Length:", k, v)
            if isinstance(rules["a"][0], int):
                return rules["a"][0]


def part_b():
    rules = {}
    for rule in pz_input:
        if rule == "":
            continue
        pieces = rule.split(" -> ")
        logic = pieces[0].split(" ")
        if len(logic) == 1:
            rules[pieces[1]] = [logic[0]]
        elif len(logic) == 2:
            rules[pieces[1]] = [logic[1], "NOT"]
        elif len(logic) == 3:
            rules[pieces[1]] = [logic[0], logic[1], logic[2]]
        else:
            raise ValueError("Invalid Length:", logic)
    rules["b"] = [16076]
    while True:
        for k in rules:
            v = rules[k]
            if len(v) == 1:
                if isinstance(v[0], str) and v[0].isnumeric():
                    rules[k] = [int(v[0])]
                elif isinstance(v[0], str) and len(rules[v[0]]) == 1 and isinstance(rules[v[0]][0], int):
                    rules[k] = [rules[v[0]][0]]
            elif len(v) == 2:
                if len(rules[v[0]]) == 1 and isinstance(rules[v[0]][0], int) and v[1] == "NOT":
                    rules[k] = [~rules[v[0]][0]]
            elif len(v) == 3:
                for i in range(0, 3, 2):
                    v[i] = int(v[i]) if isinstance(v[i], str) and v[i].isnumeric() else v[i]
                if ((isinstance(v[0], str) and len(rules[v[0]]) == 1 and isinstance(rules[v[0]][0], int)) or isinstance(
                        v[0], int)) and ((isinstance(v[2], str) and len(rules[v[2]]) == 1 and isinstance(rules[v[2]][0],
                                                                                                         int)) or isinstance(
                        v[2], int)):
                    if v[1] == "AND":
                        left = (v[0] if isinstance(v[0], int) else rules[v[0]][0])
                        right = (v[2] if isinstance(v[2], int) else rules[v[2]][0])
                        rules[k] = [left & right]
                    elif v[1] == "OR":
                        left = (v[0] if isinstance(v[0], int) else rules[v[0]][0])
                        right = (v[2] if isinstance(v[2], int) else rules[v[2]][0])
                        rules[k] = [left | right]
                    elif v[1] == "RSHIFT":
                        left = (v[0] if isinstance(v[0], int) else rules[v[0]][0])
                        right = (v[2] if isinstance(v[2], int) else rules[v[2]][0])
                        rules[k] = [left >> right]
                    elif v[1] == "LSHIFT":
                        left = (v[0] if isinstance(v[0], int) else rules[v[0]][0])
                        right = (v[2] if isinstance(v[2], int) else rules[v[2]][0])
                        rules[k] = [left << right]
                    else:
                        raise ValueError("Unknown Command:", v[1])
            else:
                raise ValueError("Invalid Length:", k, v)
            if isinstance(rules["a"][0], int):
                return rules["a"][0]


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
