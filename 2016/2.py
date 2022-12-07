"""
1 2 3
4 5 6
7 8 9

ULL
RRDDD
LURDL
UUUUD

You start at "5" and move up (to "2"), left (to "1"), and left (you can't, and
stay on "1"), so the first button is 1.

Starting from the previous button ("1"), you move right twice (to "3") and then
down three times (stopping at "9" after two moves and ignoring the third),
ending up with 9.

Continuing from "9", you move left, up, right, down, and left, ending with 8.
Finally, you move up four times (stopping at "2"), then down once, ending with
5.

    1
  2 3 4
5 6 7 8 9
  A B C
    D
"""

with open("2-input.txt", "r") as f:
    input_ = [line.strip() for line in f.readlines()]


test_in_out = [
    ("ULL", 1),
    ("RRDDD", 9),
    ("LURDL", 8),
    ("UUUUD", 5),
    ]

mapping2 = {
    "1": {"D": "3"},
    "2": {"R": "3", "D": "6"},
    "3": {"U": "1", "R": "4", "D": "7", "L": "2"},
    "4": {"D": "8", "L": "3"},
    "5": {"R": "6"},
    "6": {"D": "A", "L": "5", "U": "2", "R": "7"},
    "7": {"U": "3", "R": "8", "D": "B", "L": "6"},
    "8": {"U": "4", "R": "9", "D": "C", "L": "7"},
    "9": {"L": "8"},
    "A": {"U": "6", "R": "B"},
    "B": {"U": "7", "R": "C", "D": "D", "L": "A"},
    "C": {"U": "8", "L": "B"},
    "D": {"U": "B"},
}

mapping = {
    1: {"R": 2, "D": 4},
    2: {"R": 3, "D": 5, "L": 1},
    3: {"D": 6, "L": 2},
    4: {"R": 5, "D": 7, "U": 1},
    5: {"R": 6, "D": 8, "L": 4, "U": 2},
    6: {"D": 9, "L": 5, "U": 3},
    7: {"U": 4, "R": 8},
    8: {"U": 5, "R": 9, "L": 7},
    9: {"U": 6, "L": 8},
    }


def part1():

    def calculate(line, start):
        current = start
        for letter in line:
            current = mapping[current].get(letter, current)
        return current

    # Testing
    start = 5
    for in_, out_ in test_in_out:
        print("For %s we expect %s" % (in_, out_))
        result = calculate(in_, start)
        print("%s: worked? %s" % (result, result == out_))
        if result != out_:
            print("Aborting.")
            break
        else:
            start = result

    # The real thing
    result = ""
    start = 5
    for line in input_:
        start = calculate(line, start)
        result += str(start)
    print("Solution: %s" % result)


def part2():

    def calculate(line, start):
        current = start
        for letter in line:
            current = mapping2[current].get(letter, current)
        return current

    # Testing
    result = ""
    start = "5"
    for in_, out_ in test_in_out:
        start = calculate(in_, start)
        result += start
    print("Test expected 5DB3; got %s" % result)

    # The real thing
    result = ""
    start = "5"
    for line in input_:
        start = calculate(line, start)
        result += str(start)
    print("Solution: %s" % result)


part2()
