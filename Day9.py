from PuzzleInput import ReadInput
from collections import defaultdict

pz_input = ReadInput(9).data


def part_a():
    routes = defaultdict(lambda: {})
    for route in pz_input:
        if route == "":
            continue
        pieces = route.split(" = ")
        dist = int(pieces[1])
        destinations = pieces[0].split(" to ")
        routes[destinations[0]][destinations[1]] = dist
        routes[destinations[1]][destinations[0]] = dist
    paths = [([key], 0) for key in routes.keys()]
    finished_paths = []
    while len(paths) > 0:
        current_path = paths.pop()
        path = current_path[0]
        dist = current_path[1]
        for key in routes[path[-1]]:
            if key not in path:
                new_path = path.copy()
                new_path.append(key)
                new_dist = dist + routes[path[-1]][key]
                if len(new_path) == len(routes):
                    finished_paths.append((new_path, new_dist))
                else:
                    paths.append((new_path, new_dist))
    return min([path[1] for path in finished_paths])


def part_b():
    routes = defaultdict(lambda: {})
    for route in pz_input:
        if route == "":
            continue
        pieces = route.split(" = ")
        dist = int(pieces[1])
        destinations = pieces[0].split(" to ")
        routes[destinations[0]][destinations[1]] = dist
        routes[destinations[1]][destinations[0]] = dist
    paths = [([key], 0) for key in routes.keys()]
    finished_paths = []
    while len(paths) > 0:
        current_path = paths.pop()
        path = current_path[0]
        dist = current_path[1]
        for key in routes[path[-1]]:
            if key not in path:
                new_path = path.copy()
                new_path.append(key)
                new_dist = dist + routes[path[-1]][key]
                if len(new_path) == len(routes):
                    finished_paths.append((new_path, new_dist))
                else:
                    paths.append((new_path, new_dist))
    return max([path[1] for path in finished_paths])



if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
