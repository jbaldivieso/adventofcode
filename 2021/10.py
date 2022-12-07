from statistics import median

from utils import parse_as_str


test_input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""


OPENERS = "[({<"
PAIRS = {
    "]": "[",
    ")": "(",
    "}": "{",
    ">": "<",
}


def handle_line(line):
    """Return score if corrupt, else 0"""
    stack = []
    scores = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    for char in line:
        if char in OPENERS:
            stack.append(char)
        else:
            if stack and stack[-1] == PAIRS[char]:
                stack.pop()
            else:
                return scores[char]
    return 0


def p1(data):
    return sum([handle_line(line) for line in data])


def p2(data):
    scores = []
    PAIRS_REVERSED = {v: k for k, v in PAIRS.items()}

    def handle_line(line):
        stack = []
        for char in line:
            if char in OPENERS:
                stack.append(char)
            else:
                if stack and stack[-1] == PAIRS[char]:
                    stack.pop()
                else:
                    return
        series = [PAIRS_REVERSED[char] for char in stack]
        series.reverse()
        return series

    for line in data:
        series = handle_line(line)
        if series:
            scores.append(score_autocompletion(series))
    return median(scores)


def score_autocompletion(series):
    scores = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    score = 0
    for char in series:
        score *= 5
        score += scores[char]
    return score


if __name__ == "__main__":
    test_input = test_input.split()
    real_input = parse_as_str("10-input.txt")
    assert(p1(test_input) == 26397)
    print(p1(real_input))
    tests = [
        ("}}]])})]", 288957),
        (")}>]})", 5566),
        ("}}>}>))))", 1480781),
        ("]]}}]}]}>", 995444),
        ("])}>", 294),
    ]
    for series, expected in tests:
        got = score_autocompletion(series)
        assert got == expected, f"received: {got}, expected: {expected}"
    got = p2(test_input)
    expected = 288957
    assert got == expected, f"p2 test: received: {got}, expected: {expected}"
    print(p2(real_input))
