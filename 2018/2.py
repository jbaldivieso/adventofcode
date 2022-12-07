from collections import Counter

from utils import parseAsStr


data = parseAsStr("2-input.txt")


# ==========
# = Part 1 =
# ==========
def get2sAnd3s(s):
    """Return tuple of 1 or 0s depending on whether there were 1+ instances of:
    - a letter repeated exactly twice
    - a letter repeated exactly thrice
    """
    c = Counter(s)
    c2 = Counter(c.values())
    return (int(bool(c2.get(2, 0))), int(bool(c2.get(3, 0))))


def part1(data):
    tuples = [get2sAnd3s(s) for s in data]
    two_count, thr_count = [sum(l) for l in zip(*tuples)]
    return two_count * thr_count


assert(get2sAnd3s("abcdef") == (0, 0))
assert(get2sAnd3s("bababc") == (1, 1))
assert(get2sAnd3s("abbcde") == (1, 0))
assert(get2sAnd3s("abcccd") == (0, 1))
assert(get2sAnd3s("aabcdd") == (1, 0))
assert(get2sAnd3s("abcdee") == (1, 0))
assert(get2sAnd3s("ababab") == (0, 1))
test1Data = ("abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab")
assert(part1(test1Data) == 12)
print("Made it through part1 tests")

print(f"Part 1: {part1(data)}")


# ==========
# = Part 2 =
# ==========
def get_difference(a, b):
    """Return the number of characters that a and b differ by"""
    return sum(1 for i in range(len(a)) if a[i] != b[i])


def part2(data):
    while data:
        el = data.pop()
        for comp in data:
            if get_difference(el, comp) == 1:
                return "".join(c for i, c in enumerate(el) if c == comp[i])
    print("Failure: no result")


test_data = [
    "abcde",
    "fghij",
    "klmno",
    "pqrst",
    "fguij",
    "axcye",
    "wvxyz",
    ]
assert(part2(test_data) == "fgij")
print("Made it through part2 tests")

print(f"Part 2: {part2(data)}")
