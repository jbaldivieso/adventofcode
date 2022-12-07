from utils import parse_as_str


test_input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""

step_tests = [
    """
11111
19991
19191
19991
11111""",
    """34543
40004
50005
40004
34543
""",
    """45654
51115
61116
51115
45654"""
]


class Octopus(object):
    energy = 0
    flashed = False

    def __init__(self, energy):
        self.energy = energy

    def __str__(self):
        return f"Octo: {self.energy}"

    def reset(self):
        self.energy = 0
        self.flashed = False

    def flash(self):
        self.flashed = True

    def step(self):
        self.energy += 1


def gridify(s: str) -> list[list[int]]:
    grid = []
    for line in s:
        if not line:
            continue
        grid.append([Octopus(int(c)) for c in line])
    return grid


def take_step(grid):
    """Return a new grid after taking a step. Octopuses that flash will be set
    to 0.
    """
    width = len(grid[0])
    depth = len(grid)

    def flash(x, y):
        deltas = [
            (0, 1),  # up
            (1, 1),  # upper right
            (1, 0),  # right
            (1, -1),  # lower right
            (0, -1),  # down
            (-1, -1),  # lower left
            (-1, 0),  # left
            (-1, -1),  # upper left
        ]
        grid[y][x].flash()
        for delta in deltas:
            x1, y1 = x + delta[0], y + delta[1]
            if 0 <= x1 <= width and 0 <= y1 <= depth:
                octo = grid[y1][x1]
                octo.step()
                if octo.energy > 9 and not octo.flashed:
                    flash(x1, y1)

    # Increment all
    for row in grid:
        for octo in row:
            octo.step()

    # Calculate the knock on effect of flashes
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            octo = grid[y][x]
            if octo.energy > 9 and not octo.flashed:
                flash(x, y)

    # Reset
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            octo = grid[y][x]
            if octo.energy > 9:
                octo.reset()

    return grid


def p1(grid, steps):
    flashes = 0
    for i in range(steps):
        grid = take_step(grid)
        flashes += sum([row.count(0) for row in grid])
    return flashes


def print_grid(grid):
    for row in grid:
        for octo in row:
            print(octo.energy, end="")
        print()


if __name__ == "__main__":
    test_input = gridify(test_input.split())
    step_tests = [gridify(t.split()) for t in step_tests]
    wanted = step_tests[1]
    import ipdb; ipdb.set_trace()
    got = take_step(step_tests[0])
    try:
        assert wanted == got
    except AssertionError:
        print("Wanted")
        print_grid(wanted)
        print("Got")
        print_grid(got)
        raise
    wanted = step_tests[2]
    got = take_step(step_tests[1])
    assert wanted == got, f"Wanted:\n{print_grid(wanted)}\nGot:\n{print_grid(got)}"
    assert(p1(test_input, steps=100) == 1656)
    real_input = gridify(parse_as_str("11-input.txt"))
    print(p1(real_input), steps=100)
