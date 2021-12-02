from copy import deepcopy
from IPython.core import debugger
debug = debugger.Pdb().set_trace


test_input = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""


def apply_rules(config):
    new_config = deepcopy(config)

    def get_adjacent_count(x, y):
        """Return the number of *occupied* adjacent seats"""
        count = 0
        deltas = [
            (-1, -1), (0, -1), (1, -1),
            (-1, 0),           (1, 0),
            (-1, 1),  (0, 1),  (1, 1),
            ]
        for dx, dy in deltas:
            if (y + dy < 0) or (x + dx < 0):
                continue
            try:
                if config[y + dy][x + dx] == "#":
                    count += 1
            except IndexError:
                pass
        return count

    def update_seat(x, y):
        """Seat filling rules:
        1. If a seat is empty (L) and there are no occupied seats adjacent to
        it, the seat becomes occupied.
        2. If a seat is occupied (#) and four or more seats adjacent to it are
        also occupied, the seat becomes empty.
        3. Otherwise, the seat's state does not change.
        """
        status = new_config[y][x]
        if status == "L":
            if get_adjacent_count(x, y) == 0:
                new_config[y][x] = "#"
        elif status == "#":
            if get_adjacent_count(x, y) >= 4:
                new_config[y][x] = "L"

    for y in range(len(new_config)):
        for x in range(len(new_config[y])):
            update_seat(x, y)
    return new_config


def apply_new_rules(config):
    new_config = deepcopy(config)

    def get_adjacent_count(x, y):
        """Return the number of *occupied* adjacent seats, based on sightline.
        """
        def occupied_in_sight(x, y, dx, dy):
            if (y + dy < 0) or (x + dx < 0):
                return False
            try:
                if config[y + dy][x + dx] == "#":
                    return True
                if config[y + dy][x + dx] == ".":
                    return occupied_in_sight(x + dx, y + dy, dx, dy)
            except IndexError:
                return False

        count = 0
        deltas = [
            (-1, -1), (0, -1), (1, -1),
            (-1, 0),           (1, 0),
            (-1, 1),  (0, 1),  (1, 1),
            ]
        for dx, dy in deltas:
            if occupied_in_sight(x, y, dx, dy):
                count += 1
        return count

    def update_seat(x, y):
        """Seat filling rules:
        1. If a seat is empty (L) and there are no occupied seats adjacent to
        it, the seat becomes occupied.
        2. If a seat is occupied (#) and five or more seats adjacent to it are
        also occupied, the seat becomes empty.
        3. Otherwise, the seat's state does not change.
        """
        status = new_config[y][x]
        if status == "L":
            if get_adjacent_count(x, y) == 0:
                new_config[y][x] = "#"
        elif status == "#":
            if get_adjacent_count(x, y) >= 5:
                new_config[y][x] = "L"

    for y in range(len(new_config)):
        for x in range(len(new_config[y])):
            update_seat(x, y)
    return new_config


def count_occupied(config):
    return sum(row.count("#") for row in config)


def p1(data):
    old_config = data
    count = 1
    # debug()
    while True:
        new_config = apply_rules(old_config)
        count += 1
        if new_config == old_config:
            return count_occupied(new_config)
        old_config = new_config


def p2(data):
    old_config = data
    count = 1
    # debug()
    while True:
        new_config = apply_new_rules(old_config)
        count += 1
        if new_config == old_config:
            return count_occupied(new_config)
        old_config = new_config


if __name__ == "__main__":
    with open("11-input.txt") as f:
        data = [l.strip() for l in f.readlines()]
    # Turn data into a list of list, so we can update individual seats
    data = [list(l) for l in data if l]
    test_input = [list(l) for l in test_input.split("\n") if l]
    assert(p1(test_input) == 37)
    print(p1(data))
    assert(p2(test_input) == 26)
    print(p2(data))
