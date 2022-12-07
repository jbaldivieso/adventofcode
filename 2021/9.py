from utils import parse_as_str


test_input = """
2199943210
3987894921
9856789892
8767896789
9899965678
"""


def parse_input(lines: list) -> list:
    return [[int(i) for i in line] for line in lines]


def get_low_points(data):
    lows = []
    width = len(data[0])
    depth = len(data)
    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            up = (x, y - 1)
            down = (x, y + 1)
            left = (x - 1, y)
            right = (x + 1, y)
            to_check = [up, down, left, right]
            if y == 0:
                del to_check[to_check.index(up)]
            elif y == depth - 1:
                del to_check[to_check.index(down)]
            if x == 0:
                del to_check[to_check.index(left)]
            elif x == width - 1:
                del to_check[to_check.index(right)]
            if all([cell < data[y_][x_] for x_, y_ in to_check]):
                lows.append((x, y))
    return lows


def p1(data):
    lows = [data[y][x] for x, y in get_low_points(data)]
    return sum(lows) + len(lows)


def get_basin_size(data, x, y):
    width = len(data[0])
    depth = len(data)
    seen = set()
    to_search = [(x, y)]
    directions = [
        (0, 1),  # up
        (0, -1),  # down
        (1, 0),  # right
        (-1, 0),  # left
        ]
    while to_search:
        current = to_search.pop()
        seen.add(current)
        for delta in directions:
            new = (current[0] + delta[0], current[1] + delta[1])
            if (
                # In our grid?
                0 <= new[0] < width and 0 <= new[1] < depth
                and
                new not in seen
                and
                data[new[1]][new[0]] != 9
                    ):
                to_search.append(new)
    return len(seen)


def p2(data):
    basin_sizes = [get_basin_size(data, x, y) for x, y in get_low_points(data)]
    basin_sizes.sort(reverse=True)
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


if __name__ == "__main__":
    test_input = parse_input(test_input.split())
    real_input = parse_input(parse_as_str("9-input.txt"))
    assert(p1(test_input) == 15)
    print(p1(real_input))
    test_values = [
        (1, 0, 3),
        (9, 0, 9),
        (2, 2, 14),
        (6, 4, 9),
    ]
    for x, y, expected in test_values:
        received = get_basin_size(test_input, x, y)
        assert expected == received, f"wanted: {expected}, got: {received}"
    expected = 1134
    received = p2(test_input)
    assert expected == received, f"wanted: {expected}, got: {received}"
    print(p2(real_input))
