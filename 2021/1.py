from utils import parse_as_ints


test_input = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]


def p1(input):
    return len([
        1 for x in range(1, len(input))
        if input[x] > input[x - 1]
    ])


def p2(input):
    # Because the groups overlap with two of their elements, the only comparison
    # we really care about is x vs x-3.
    return len([
        1 for x in range(3, len(input))
        if input[x] > input[x - 3]
    ])


if __name__ == "__main__":
    assert(p1(test_input) == 7)
    print(p1(parse_as_ints("1-input.txt")))
    assert(p2(test_input) == 5)
    print(p2(parse_as_ints("1-input.txt")))
