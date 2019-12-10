from PuzzleInput import ReadInput
import numpy as np

pz_input = ReadInput(18).data


def part_a():
    grid = (np.array([list(x) for x in pz_input if len(x) > 0]) == "#").astype(int)
    for i in range(100):
        curr_state = grid.copy()
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                neighbors = curr_state[max(0, y - 1):min(len(grid), y + 2), max(0, x - 1):min(len(grid), x + 2)]
                if grid[y, x] == 1:
                    grid[y, x] = 1 if 3 <= neighbors.sum() <= 4 else 0
                else:
                    grid[y, x] = 1 if neighbors.sum() == 3 else 0
    return grid.sum()


def part_b():
    grid = (np.array([list(x) for x in pz_input if len(x) > 0]) == "#").astype(int)
    grid[0, 0] = 1
    grid[99, 0] = 1
    grid[0, 99] = 1
    grid[99, 99] = 1
    for i in range(100):
        curr_state = grid.copy()
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if (x == 0 and y == 0) or (x == 0 and y == 99) or (x == 99 and y == 0) or (x == 99 and y == 99):
                    continue
                neighbors = curr_state[max(0, y - 1):min(len(grid), y + 2), max(0, x - 1):min(len(grid), x + 2)]
                if grid[y, x] == 1:
                    grid[y, x] = 1 if 3 <= neighbors.sum() <= 4 else 0
                else:
                    grid[y, x] = 1 if neighbors.sum() == 3 else 0
    return grid.sum()


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
