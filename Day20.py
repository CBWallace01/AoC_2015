from collections import defaultdict

pz_input = 33100000


def part_a():
    house = 720000
    # house = 1
    while True:
        factors = [x for x in range(1, int(pz_input**0.5)+1) if house % x == 0]
        factors.extend([house//x for x in factors if house//x not in factors])
        if house not in factors:
            factors.append(house)
        total = sum(factors)
        if house % 10000 == 0:
            print(house)
        if total >= pz_input/10:
            return house, total * 10
        else:
            house += 1


def part_b():
    # house = 720000
    house = 1
    visited = defaultdict(lambda: 0)
    while True:
        factors = [x for x in range(1, int(pz_input ** 0.5) + 1) if house % x == 0 and visited[x] <= 50]
        factors.extend([house // x for x in factors if house // x not in factors and visited[house//x]<=50])
        if house not in factors:
            factors.append(house)
        for factor in factors:
            visited[factor] += 1
        total = sum(factors)
        if house % 10000 == 0:
            print(house)
        if total * 11 >= pz_input:
            return house, total * 11
        else:
            house += 1


if __name__ == "__main__":
    # print("Part A", part_a())
    print("Part B", part_b())
