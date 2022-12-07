import sys

from utils import parse_as_str


# ==========
# = Part 1 =
# ==========
test1_data = "dabAcCaCBAcCcaDA"

data = parse_as_str("5-input.txt")[0]


def test_pair(a, b):
    return (a != b) and ((a.upper() == b.upper()))


print(f"Recursion limit WAS {sys.getrecursionlimit()}")
sys.setrecursionlimit(sys.getrecursionlimit() * 100)
print(f"Now it's {sys.getrecursionlimit()}")


def part1(data):
    def shrink_string(s):
        for i in range(len(s) - 1):
            if test_pair(s[i], s[i + 1]):
                return shrink_string(s[:i] + s[i + 2:])
        return s
    return len(shrink_string(data))


assert part1(test1_data) == 10
print("Made it through Part 1 tests")
# print(f"Part 1: {part1(data)}")
# Returns 11476; takes a long time as written!


# ==========
# = Part 2 =
# ==========
def part2(data):
    uniques = {c.lower() for c in data}
    best = len(data)
    for letter in uniques:
        print(f"Now looking at {letter}")
        s = data.replace(letter, "").replace(letter.upper(), "")
        this_version = part1(s)
        best = this_version if this_version < best else best
        print(f"Resulting in {this_version}")
    return best


assert part2(test1_data) == 4
print("Made it through the part 2 tests")
print(f"Part 2 result: {part2(data)}")
