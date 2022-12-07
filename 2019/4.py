puzzle_input = (359282, 820401)
test_input = [
    (111111, True),
    (223450, False),
    (123789, False),
    ]

test2_input = [
    (112233, True),
    (123444, False),
    (111122, True),
    ]


def is_valid(i, use_extra_test=False):
    """Criteria:
    * It is a six-digit number. (assumed to be True)
    * The value is within the range given in your puzzle input. (Ditto)
    * Two adjacent digits are the same (like 22 in 122345).
    * Going from left to right, the digits never decrease; they only ever
      increase or stay the same (like 111123 or 135679).
    """
    def has_doubled_digits(l):
        return any([l[i] == l[i + 1] for i in range(len(l) - 1)])

    def never_decreases(l):
        return all([l[i] <= l[i + 1] for i in range(len(l) - 1)])

    def extra_test(l):
        prev = None
        likeness_counts = []
        likeness_count = 0
        for i in l:
            if prev == i:
                likeness_count += 1
            else:
                if likeness_count:
                    likeness_counts.append(likeness_count)
                likeness_count = 1
                prev = i
        likeness_counts.append(likeness_count)
        return 2 in likeness_counts

    # Turn our input i into a list of ints
    as_list = [int(c) for c in str(i)]
    result = has_doubled_digits(as_list) and never_decreases(as_list)
    if use_extra_test:
        return result and extra_test(as_list)
    else:
        return result


def part1():
    return len([1 for v in range(*puzzle_input) if is_valid(v)])


def part2():
    return len([1 for v in range(*puzzle_input) if is_valid(v, use_extra_test=True)])


for i, expected in test_input:
    assert is_valid(i) == expected
print(f"Part 1: {part1()}")

for i, expected in test2_input:
    print(f"Got {is_valid(i, use_extra_test=True)}, expected: {expected}")

assert is_valid(i, use_extra_test=True) == expected
print(f"Part 2: {part2()}")
