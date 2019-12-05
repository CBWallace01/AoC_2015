from PuzzleInput import ReadInput
import numpy as np

pz_input = ReadInput(6).data


def part_a():
    grid = np.ones((1000, 1000))
    grid *= -1

    for instruction in pz_input:
        bits = instruction.split(" ")
        if bits[0] == "turn":
            corner_1 = bits[2].split(",")
            corner_2 = bits[4].split(",")
            grid[int(corner_1[0]):int(corner_2[0])+1, int(corner_1[1]):int(corner_2[1])+1] = 1 if bits[1] == "on" else -1
        elif bits[0] == "toggle":
            corner_1 = bits[1].split(",")
            corner_2 = bits[3].split(",")
            grid[int(corner_1[0]):int(corner_2[0]) + 1, int(corner_1[1]):int(corner_2[1]) + 1] *= -1
    grid += 1
    return np.count_nonzero(grid)


def part_b():
    grid = np.zeros((1000, 1000))

    for instruction in pz_input:
        bits = instruction.split(" ")
        if bits[0] == "turn":
            corner_1 = bits[2].split(",")
            corner_2 = bits[4].split(",")
            grid[int(corner_1[0]):int(corner_2[0]) + 1, int(corner_1[1]):int(corner_2[1]) + 1] += 1 if bits[1] == "on" else -1
        elif bits[0] == "toggle":
            corner_1 = bits[1].split(",")
            corner_2 = bits[3].split(",")
            grid[int(corner_1[0]):int(corner_2[0]) + 1, int(corner_1[1]):int(corner_2[1]) + 1] += 2
        grid = np.where(grid >= 0, grid, 0)
    return np.sum(grid)


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
