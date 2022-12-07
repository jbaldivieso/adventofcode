import statistics as stats

from utils import parse_as_ints

test_input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def p1(data):
    expected_range = sorted([round(stats.mean(data)), round(stats.median(data))])
    fuel_costs = []
    for x in range(*expected_range):
        fuel_costs.append(sum([abs(v - x) for v in data]))
    return min(fuel_costs)


def p2(data):
    cost_map = {x: sum(range(x+1)) for x in range(max(data) + 1)}
    expected_range = sorted([round(stats.mean(data)), round(stats.median(data))])
    expected_range = [expected_range[0] - 2, expected_range[1] + 2]
    fuel_costs = []
    for x in range(*expected_range):
        fuel_costs.append(sum([cost_map[abs(v - x)] for v in data]))
    return min(fuel_costs)


if __name__ == "__main__":
    real_input = parse_as_ints("7-input.txt", delimiter=",")
    assert(p1(test_input.copy()) == 37)
    print(p1(real_input.copy()))
    try:
        expected = 168
        received = p2(test_input)
        assert(expected == received)
    except AssertionError:
        print(f"Expected: {expected}; received: {received}")
        raise
    print(p2(real_input))
