test_input = """
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""


def test(data, i, preamble):
    """Return True if data[i] meets puzzle criteria"""
    target = data[i]
    slice = set(data[i - preamble:i])
    for option in slice:
        if target - option in slice:
            return True
    return False


def p1(data, preamble=25):
    for i in range(len(data)):
        if i + 1 <= preamble:
            continue
        if not test(data, i, preamble):
            return data[i]


def p2(data, preamble=25):
    invalid = p1(data, preamble)
    size = len(data)
    for i in range(len(data)):
        for j in range(1, size - i):
            slice = data[i:j]
            sum_ = sum(slice)
            if sum_ == invalid:
                return sum((min(slice), max(slice)))
            if sum_ > invalid:
                break


if __name__ == "__main__":
    with open("9-input.txt") as f:
        data = [l.strip() for l in f.readlines()]
    data = [int(l) for l in data if l]
    test_input = [int(l) for l in test_input.split("\n") if l.strip()]
    assert(p1(test_input, 5) == 127)
    print(p1(data))
    assert(p2(test_input, 5) == 62)
    print(p2(data))
