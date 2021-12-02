from IPython.core import debugger
debug = debugger.Pdb().set_trace

test_input = """
F10
N3
F7
R90
F11
"""


def process_instruction(pos, ori, inst, dist):
    if inst == "L":
        ori -= dist
        if ori < 0:
            ori += 360
        return pos, ori
    if inst == "R":
        ori += dist
        if ori >= 360:
            ori -= 360
        return pos, ori
    if inst == "N" or (inst == "F" and ori == 0):
        delta = [0, dist]
    elif inst == "E" or (inst == "F" and ori == 90):
        delta = [-dist, 0]
    elif inst == "S" or (inst == "F" and ori == 180):
        delta = [0, -dist]
    elif inst == "W" or (inst == "F" and ori == 270):
        delta = [dist, 0]
    return [pos[0] + delta[0], pos[1] + delta[1]], ori


def process_instruction2(ship, waypoint, inst, dist):
    if inst in ("L", "R"):
        invert = True
        if dist == 90:
            multiplier = (-1, 1) if inst == "R" else (1, -1)
        elif dist == 180:
            multiplier = (-1, -1)
            invert = False
        elif dist == 270:
            multiplier = (1, -1) if inst == "R" else (-1, 1)
        else:
            raise Exception(f"Unexpected rotation angle: {dist}")
        waypoint = [waypoint[0] * multiplier[0], waypoint[1] * multiplier[1]]
        if invert:
            waypoint = [waypoint[1], waypoint[0]]
        return ship, waypoint
    if inst == "F":
        ship = [ship[0] + (dist * waypoint[0]), ship[1] + (dist * waypoint[1])]
        return ship, waypoint
    if inst == "N":
        delta = [0, dist]
    elif inst == "E":
        delta = [-dist, 0]
    elif inst == "S":
        delta = [0, -dist]
    elif inst == "W":
        delta = [dist, 0]
    return ship, [waypoint[0] + delta[0], waypoint[1] + delta[1]]


def p1(data):
    pos, ori = [0, 0], 90
    for inst, dist in [(r[0], int(r[1:])) for r in data]:
        pos, ori = process_instruction(pos, ori, inst, dist)
    return abs(pos[0]) + abs(pos[1])


def p2(data):
    ship = [0, 0]
    waypoint = [0, 0]
    for inst, dist in [(r[0], int(r[1:])) for r in data]:
        ship, waypoint = process_instruction2(ship, waypoint, inst, dist)
    return abs(ship[0]) + abs(ship[1])


if __name__ == "__main__":
    with open("12-input.txt") as f:
        data = [l.strip() for l in f.readlines() if l.strip()]
    test_input = [l for l in test_input.split("\n") if l]
    assert(p1(test_input) == 25)
    print(p1(data))
    assert(p2(test_input) == 286)
    print(p2(data))
