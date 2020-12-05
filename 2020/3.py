test_input = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""


def prod(iter):
    result = 1
    for x in iter:
        result *= x
    return result


def p1(data):
    # right 3, down 1
    x = 0
    trees = 0

    def is_a_tree(row, x):
        index = x % len(row)
        return row[index] == "#"

    for i, row in enumerate(data):
        if is_a_tree(row, x):
            trees += 1
        x += 3
        # print(f"At row {i} we had {trees} trees.")
    return trees


def p2(data):
    def is_a_tree(x, y):
        index = x % len(data[0])
        return data[y][index] == "#"

    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
        ]

    trees_per_slope = []
    for over, down in slopes:
        x = 0
        y = 0
        trees = 0
        while y < len(data):
            if is_a_tree(x, y):
                trees += 1
            # print(f"At {x}, {y} we had {trees} trees (at {data[y]}).")
            x += over
            y += down
        trees_per_slope.append(trees)
        # print(f"For slope ({over}, {down}), we got {trees}.")
    return prod(trees_per_slope)


if __name__ == "__main__":
    test_input = test_input.split()
    assert(p1(test_input) == 7)
    with open("3-input.txt") as f:
        data = [line.strip() for line in f.readlines()]
    print(p1(data))
    assert(p2(test_input) == 336)
    print(p2(data))
