from utils import parseAsInts


# ==========
# = Part 1 =
# ==========
def part1(data):
    """data is an iterable of ints"""
    return sum(data)


# Tests
assert(part1((+1, +1, +1)) == 3)
assert(part1((+1, +1, -2)) == 0)
assert(part1((-1, -2, -3)) == -6)

data = parseAsInts("1-input.txt")

p1 = part1(data)

print(f"Part 1: {p1}")


# ==========
# = Part 2 =
# ==========
def part2(data):
    already_seen = {0}
    freq = 0
    while True:
        for val in data:
            freq += val
            if freq in already_seen:
                return freq
            else:
                already_seen.add(freq)


assert(part2((+1, -1)) == 0)
assert(part2((+3, +3, +4, -2, -4)) == 10)
assert(part2((-6, +3, +8, +5, -6)) == 5)
assert(part2((+7, +7, -2, -7, -4)) == 14)


print(f"Part 2: {part2(data)}")
