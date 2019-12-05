from PuzzleInput import ReadInput

pz_input = ReadInput(15).data


def part_a():
    ingredients = []
    max_score = 0
    for item in pz_input:
        if item == "":
            continue
        pieces = item.split(" ")
        ingredients.append([int(pieces[2][:-1]), int(pieces[4][:-1]), int(pieces[6][:-1]), int(pieces[8][:-1]), int(pieces[10])])
    amount = [0] * 4
    while amount[0] < 100:
        for i in range(len(ingredients)-1, -1, -1):
            amount[i] += 1
            if amount[i] <= 100:
                break
            else:
                amount[i] = 0
        if sum(amount) != 100:
            continue
        capacity = 0
        durability = 0
        flavor = 0
        texture = 0
        for i in range(len(ingredients)):
            capacity += ingredients[i][0] * amount[i]
            durability += ingredients[i][1] * amount[i]
            flavor += ingredients[i][2] * amount[i]
            texture += ingredients[i][3] * amount[i]
        curr_score = capacity * durability * flavor * texture if capacity > 0 and durability > 0 and flavor > 0 and texture > 0 else 0
        if curr_score > max_score:
            max_score = curr_score
    return max_score


def part_b():
    ingredients = []
    max_score = 0
    for item in pz_input:
        if item == "":
            continue
        pieces = item.split(" ")
        ingredients.append(
            [int(pieces[2][:-1]), int(pieces[4][:-1]), int(pieces[6][:-1]), int(pieces[8][:-1]), int(pieces[10])])
    amount = [0] * 4
    while amount[0] < 100:
        for i in range(len(ingredients) - 1, -1, -1):
            amount[i] += 1
            if amount[i] <= 100:
                break
            else:
                amount[i] = 0
        if sum(amount) != 100:
            continue
        capacity = 0
        durability = 0
        flavor = 0
        texture = 0
        calories = 0
        for i in range(len(ingredients)):
            capacity += ingredients[i][0] * amount[i]
            durability += ingredients[i][1] * amount[i]
            flavor += ingredients[i][2] * amount[i]
            texture += ingredients[i][3] * amount[i]
            calories += ingredients[i][4] * amount[i]
        curr_score = capacity * durability * flavor * texture if capacity > 0 and durability > 0 and flavor > 0 and texture > 0 else 0
        if curr_score > max_score and calories == 500:
            max_score = curr_score
    return max_score


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
