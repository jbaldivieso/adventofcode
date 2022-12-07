from utils import parse_as_ints

test_input = [
    ([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50],
     [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]),
    ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
    ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
    ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
    ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]),
    ]


def part1(data):
    for x in range(0, len(data), 4):
        if data[x] == 99:
            return data
        operation, v1, v2, out = data[x: x+4]
        try:
            if operation == 1:
                data[out] = data[v1] + data[v2]
            else:
                data[out] = data[v1] * data[v2]
        except IndexError:
            return None


for in_, out in test_input:
    assert part1(in_) == out
print("Passed part1 tests")

data = parse_as_ints("2-input.txt", delimiter=",")
# before running the program, replace position 1 with the value 12 and replace
# position 2 with the value 2.
data[1] = 12
data[2] = 2

data = part1(data)
print(f"First element of processed data: {data[0]}")


def part2():
    desired = 19690720
    data = parse_as_ints("2-input.txt", delimiter=",")
    for noun in range(100):
        for verb in range(100):
            d = data.copy()
            d[1] = noun
            d[2] = verb
            result = part1(d)
            if result and result[0] == desired:
                return noun, verb
    raise Exception("Exhausted range :-(")


noun, verb = part2()
print(f"Part2 answer: {100 * noun + verb}")
