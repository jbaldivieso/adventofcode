test_input = """
abc

a
b
c

ab
ac

a
a
a
a

b
"""


def p1(data):
    groups = data.split("\n\n")
    count = 0
    for group in groups:
        chars = [c for c in group if c.isalpha()]
        count += len(set(chars))
    return count


def p2(data):
    groups = data.split("\n\n")
    count = 0
    for group in groups:
        rows = group.split()
        if len(rows) == 1:
            count += len(rows[0])
        else:
            rows = [set(row) for row in rows]
            intersections = rows[0].intersection(*rows[1:])
            count += len(intersections)
    return count


if __name__ == "__main__":
    assert(p1(test_input) == 11)
    with open("6-input.txt") as f:
        data = f.read()
    print(p1(data))
    assert(p2(test_input) == 6)
    print(p2(data))
