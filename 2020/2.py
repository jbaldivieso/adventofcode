test_input = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc",
    ]


def parse(line):
    range_, char, pwd = line.split(" ")
    min_, max_ = [int(x) for x in range_.split("-")]
    char = char[0]
    return (min_, max_, char, pwd)


def p1(data):
    def test(min_, max_, char, pwd):
        count = pwd.count(char)
        return min_ <= count <= max_

    count = 0
    for line in data:
        if test(*parse(line)):
            count += 1
    return count


def p2(data):
    def test(pos1, pos2, char, pwd):
        sub = pwd[pos1 - 1] + pwd[pos2 - 1]
        return sub.count(char) == 1

    count = 0
    for line in data:
        if test(*parse(line)):
            count += 1
    return count


if __name__ == "__main__":
    assert(p1(test_input) == 2)
    with open("2-input.txt") as f:
        print(p1(f.readlines()))
    assert(p2(test_input) == 1)
    with open("2-input.txt") as f:
        print(p2(f.readlines()))
