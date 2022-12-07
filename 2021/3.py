from collections import Counter

from utils import parse_as_str


test_input = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


def p1(input):
    gamma = epsilon = ""
    for x in range(len(input[0])):
        values = [r[x] for r in input]
        counter = Counter(values)
        # most/least are tuples (val, count)
        most, least = counter.most_common(2)
        gamma += most[0]
        epsilon += least[0]
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma * epsilon


def p2(input):
    def get_rating(higher):
        """If @higher, use logic for O2, otherwise use CO2 logic."""
        pool = input.copy()
        for x in range(len(input[0])):
            values = [r[x] for r in pool]
            counter = Counter(values)
            # most/least are tuples (val, count)
            most, least = counter.most_common(2)
            if most[1] == least[1]:
                val = "1" if higher else "0"
            else:
                val = most[0] if higher else least[0]
            pool = [v for v in pool if v[x] == val]
            if len(pool) == 1:
                return int(pool[0], 2)
    o2 = get_rating(higher=True)
    co2 = get_rating(higher=False)
    return o2 * co2


if __name__ == "__main__":
    assert(p1(test_input) == 198)
    print(p1(parse_as_str("3-input.txt")))
    assert(p2(test_input) == 230)
    print(p2(parse_as_str("3-input.txt")))
