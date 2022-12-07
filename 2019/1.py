from math import floor

from utils import parse_as_ints


test_data = [
    (12, 2),
    (14, 2),
    (1969, 654),
    (100756, 33583),
    ]


def part1(datum):
    return floor(datum / 3) - 2


for input_, output in test_data:
    assert part1(input_) == output
print("Made it through part1 tests")
results = sum(part1(d) for d in parse_as_ints("1-input.txt"))
print(f"Part 1: {results}")


def part2(d):
    r = part1(d)
    if r <= 0:
        return 0
    return r + part2(r)


test2 = (100756, 50346)
assert part2(test2[0]) == test2[1]
result = sum(part2(d) for d in parse_as_ints("1-input.txt"))
print(f"Part 2: {result}")
