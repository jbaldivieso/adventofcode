from utils import parse_as_str


test_input = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""


def parse_input(data: list) -> list:
    """Given a list of strings, return a list of 2-tuples of coordinates (also
    2-tuples).
    """
    results = []
    for line in data:
        if not line:
            continue
        start, end = line.split(" -> ")
        results.append((eval(start), eval(end)))
    return results


def coordinate_pair2series_of_points(pair: tuple) -> list:
    """Given a coordinate pair, return a list of points that they describe.
    If the points aren't a vertical or horizontal line, the list will be empty.
    """
    results = []
    p1, p2 = pair
    # Vertical or horizontal or neither?
    if p1[0] == p2[0]:
        # Vertical
        index = 1
    elif p1[1] == p2[1]:
        # Horizontal
        index = 0
    else:
        # Neither
        return results
    # Sort them
    if p1[index] > p2[index]:
        p2, p1 = p1, p2
    for x in range(p2[index] - p1[index] + 1):
        if index == 0:
            results.append((p1[0] + x, p1[1]))
        else:
            results.append((p1[0], p1[1] + x))
    return results


def coordinate_pair2series_of_points2(pair: tuple) -> list:
    """Given a coordinate pair, return a list of points that they describe.
    If the points aren't a vertical, horizontal, or 45-degree diagonal line,
    the list will be empty.
    """
    results = []
    p1, p2 = pair
    # Vertical or horizontal or diag or neither?
    if abs(p1[0] - p2[0]) == abs(p1[1] - p2[1]):
        # Diagonal
        return extrapolate_diagonal(p1, p2)
    elif p1[0] == p2[0]:
        # Vertical
        index = 1
    elif p1[1] == p2[1]:
        # Horizontal
        index = 0
    else:
        # Neither
        return results
    # Sort them
    if p1[index] > p2[index]:
        p2, p1 = p1, p2
    for x in range(p2[index] - p1[index] + 1):
        if index == 0:
            results.append((p1[0] + x, p1[1]))
        else:
            results.append((p1[0], p1[1] + x))
    return results


def extrapolate_diagonal(p1: tuple, p2: tuple) -> list:
    results = []
    if p1[0] > p2[0]:
        x_mut = lambda x, b: x - b
    else:
        x_mut = lambda x, b: x + b
    if p1[1] > p2[1]:
        y_mut = lambda y, b: y - b
    else:
        y_mut = lambda y, b: y + b
    for i in range(abs(p1[0] - p2[0]) + 1):
        results.append((x_mut(p1[0], i), y_mut(p1[1], i)))
    return results


def p1(data: list, v: int=1) -> int:
    data = parse_input(data)
    # We'll just make a massive list of points, combining all the lines.
    points = []
    if v == 1:
        extrapolator = coordinate_pair2series_of_points
    else:
        extrapolator = coordinate_pair2series_of_points2
    for pair in data:
        points.extend(extrapolator(pair))
    x_max = max(p[0] for p in points) + 1
    y_max = max(p[1] for p in points) + 1
    grid = [[0 for p in range(x_max)] for q in range(y_max)]
    for x, y in points:
        grid[y][x] += 1
    return len([1 for x in range(x_max) for y in range(y_max) if grid[y][x] > 1])


if __name__ == "__main__":
    assert(p1(test_input.split("\n")) == 5)
    assert(p1(parse_as_str("5-input.txt")) == 5774)
    expected = {(4, 1), (3, 2), (2, 3), (1, 4)}
    received = set(extrapolate_diagonal((4, 1), (1, 4)))
    assert(expected == received)
    expected = {(4, 1), (5, 2), (6, 3)}
    received = set(extrapolate_diagonal((4, 1), (6, 3)))
    assert(expected == received)
    assert(p1(test_input.split("\n"), v=2) == 12)
    print(p1(parse_as_str("5-input.txt"), v=2))
