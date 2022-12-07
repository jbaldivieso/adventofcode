"""
{}, score of 1.
{{{}}}, score of 1 + 2 + 3 = 6.
{{},{}}, score of 1 + 2 + 2 = 5.
{{{},{},{{}}}}, score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
{<a>,<a>,<a>,<a>}, score of 1.
{{<ab>},{<ab>},{<ab>},{<ab>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
{{<!!>},{<!!>},{<!!>},{<!!>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
{{<a!>},{<a!>},{<a!>},{<ab>}}, score of 1 + 2 = 3.
"""

with open("9-input.txt", "r") as f:
    data = f.readline().strip()


def part1():

    def process(stream):
        counter = 0
        score = 0
        in_garbage = False
        prev = None

        for char in stream:
            if prev != "!":
                if in_garbage:
                    if char == ">":
                        in_garbage = False
                else:
                    if char == "{":
                        counter += 1
                    elif char == "<":
                        in_garbage = True
                    elif char == "}":
                        score += counter
                        counter -= 1
                prev = char
            else:
                prev = None  # To cancel 2 consecutive !!

        return score

    test_data = [
        ("{}", 1),
        ("{{{}}}", 6),
        ("{{},{}}", 5),
        ("{{{},{},{{}}}}", 16),
        ("{<a>,<a>,<a>,<a>}", 1),
        ("{{<ab>},{<ab>},{<ab>},{<ab>}}", 9),
        ("{{<!!>},{<!!>},{<!!>},{<!!>}}", 9),
        ("{{<a!>},{<a!>},{<a!>},{<ab>}}", 3),
        ]
    for line, expected in test_data:
        print("Test: expected %s, got %s" % (expected, process(line)))
    print("Solution: %s" % process(data))


def part2():

    def process(stream):
        garbage_count = 0
        in_garbage = False
        prev = None

        for char in stream:
            if prev != "!":
                if in_garbage:
                    if char == ">":
                        in_garbage = False
                    elif char != "!":
                        garbage_count += 1
                else:
                    if char == "<":
                        in_garbage = True
                prev = char
            else:
                prev = None  # To cancel 2 consecutive !!

        return garbage_count

    test_data = [
        ('<>', 0),
        ('<random characters>', 17),
        ('<<<<>', 3),
        ('<{!>}>', 2),
        ('<!!>', 0),
        ('<!!!>>', 0),
        ('<{o"i!a,<{i<a>', 10),
        ]
    for line, expected in test_data:
        print("Test: expected %s, got %s" % (expected, process(line)))
    print("Solution: %s" % process(data))


part2()
