from PuzzleInput import ReadInput

pz_input = ReadInput(14).data


def part_a():
    distances = []
    for reindeer in pz_input:
        if reindeer == "":
            continue
        pieces = reindeer.split(" ")
        distance = 0
        is_flying = True
        step = 1
        for i in range(2503):
            if is_flying:
                distance += int(pieces[3])
                if step == int(pieces[6]):
                    is_flying = False
                    step = 1
                    continue
            else:
                if step == int(pieces[13]):
                    is_flying = True
                    step = 1
                    continue
            step += 1
        distances.append(distance)
    return max(distances)


def part_b():
    distances = []
    reindeer = []  # [0:distance, 1:speed, 2:fly_time, 3:rest_time, 4:is_flying, 5:curr_step, 6:points]
    for deer in pz_input:
        if deer == "":
            continue
        pieces = deer.split(" ")
        reindeer.append([0, int(pieces[3]), int(pieces[6]), int(pieces[13]), True, 1, 0])

    for i in range(2503):
        for deer in reindeer:
            if deer[4]:
                deer[0] += deer[1]
                if deer[5] == deer[2]:
                    deer[4] = False
                    deer[5] = 1
                    continue
            else:
                if deer[5] == deer[3]:
                    deer[4] = True
                    deer[5] = 1
                    continue
            deer[5] += 1
        m = max([deer[0] for deer in reindeer])
        leading = [i for i, j in enumerate(reindeer) if j[0] == m]
        for n in leading:
            reindeer[n][6] += 1
    return max([deer[6] for deer in reindeer])


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
