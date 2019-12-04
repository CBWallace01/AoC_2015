import hashlib

pz_input = "bgvyzdsv"


def part_a():
    i = 1
    while True:
        to_test = (pz_input + str(i)).encode('utf-8')
        result = hashlib.md5(to_test).digest()
        if result[0] == result[1] == 0 and result[2] <= 9:
            return i
        i += 1


def part_b():
    i = 1
    while True:
        to_test = (pz_input + str(i)).encode('utf-8')
        result = hashlib.md5(to_test).digest()
        if result[0] == result[1] == result[2] == 0:
            return i
        i += 1


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
