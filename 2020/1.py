from utils import parse_as_ints

test_input = [
    1721,
    979,
    366,
    299,
    675,
    1456,
    ]


def p1(data):
    pool = set(data)
    for x in data:
        wanted = 2020 - x
        if wanted in pool:
            answer = x * wanted
            print(f"Part 1 answer: {x}, {wanted}. Multiplied: {answer}")
            return answer


def p2(data):
    pool = set(data)
    for x in data:
        for y in data:
            if y == x:
                continue
            wanted = 2020 - x - y
            if wanted in pool:
                answer = wanted * x * y
                print(f"Part 2 answer: {x}, {y}, {wanted}. Multiplied: {answer}")
                return answer


if __name__ == "__main__":
    assert(p1(test_input) == 514579)
    p1(parse_as_ints("1-input.txt"))
    assert(p2(test_input) == 241861950)
    p2(parse_as_ints("1-input.txt"))
