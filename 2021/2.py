from utils import parse_as_str


test_input = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2",
]


def parse(input):
    results = [l.split(" ") for l in input]
    results = [(cmd, int(dist)) for cmd, dist in results]
    return results


def p1(input):
    # Assuming input is already parsed
    pos = (0, 0)
    for cmd, dist in input:
        if cmd == "forward":
            pos = (pos[0] + dist, pos[1])
        elif cmd == "up":
            pos = (pos[0], pos[1] - dist)
        else:
            pos = (pos[0], pos[1] + dist)
    return pos[0] * pos[1]


def p2(input):
    # Assuming input is already parsed
    # - down X increases your aim by X units.
    # - up X decreases your aim by X units.
    # - forward X does two things:
    #   - It increases your horizontal position by X units.
    #   - It increases your depth by your aim multiplied by X.
    aim = 0
    pos = (0, 0)
    for cmd, dist in input:
        if cmd == "forward":
            pos = (pos[0] + dist, pos[1] + (aim * dist))
        elif cmd == "up":
            aim -= dist
        else:
            aim += dist
    return pos[0] * pos[1]


if __name__ == "__main__":
    assert(p1(parse(test_input)) == 150)
    print(p1(parse(parse_as_str("2-input.txt"))))
    assert(p2(parse(test_input)) == 900)
    print(p2(parse(parse_as_str("2-input.txt"))))
