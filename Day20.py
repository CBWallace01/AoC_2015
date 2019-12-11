pz_input = 33100000


def part_a():
    house = 50000
    house = 1
    while True:
        total = sum([x for x in range(1, house+1) if house % x == 0])
        if house % 10000 == 0:
            print(house, total)
        if total >= pz_input/10:
            return house, total * 10
        else:
            house += 1


def part_b():
    floor = 0
    return floor


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
