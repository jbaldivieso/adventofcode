from utils import parse_as_str


test_input = """
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""


def p1(data):
    # 1: 2 segments
    # 4: 4 segments
    # 7: 3 segments
    # 8: 7 segments
    output = [line.split(" | ")[1].split(" ") for line in data]
    # output is now a list of lists
    result = 0
    for line in output:
        result += len([1 for digit in line if len(digit) in {2, 3, 4, 7}])
    return result


def p2(data):
    return sum([decode(d) for d in data])


def convert2string(chars):
    return "".join(sorted(chars))


def decode(line):
    """
     aaa
    b   c
    b   c
     ddd
    e   f
    e   f
     ggg

    1:   c  f  (2)
    4:  bcd f  (4)
    7: a c  f  (3)
    8: abcdefg (7)

    2: a cde g (5) x
    3: a cd fg (5) x
    5: ab d fg (5) x

    6: ab defg (6) x
    9: abcd fg (6) x
    0: abc efg (6) x

    In the uniques:
    c/f: present in all of them
    b/d: present in 4 and 8
      a: present in 7 and 8
    e/g: only in 8

    Others
    f: only missing from 2
    d: only non unique without d is 0
    e: only 5-char non-unique with it: 2
    """
    sample, output = line.split(" | ")
    sample = [convert2string(word) for word in sample.split(" ")]
    output = [convert2string(word) for word in output.split(" ")]
    known = {}  # Scrambled chars: intended decimal digit
    rev_known = {}  # Intended decimal: scrambled char *sets*

    # Low hanging fruit
    for digit in sample:
        match len(digit):
            case 2:
                known[digit] = 1
            case 3:
                known[digit] = 7
            case 4:
                known[digit] = 4
            case 7:
                known[digit] = 8
    rev_known = {v: set(chars) for chars, v in known.items()}

    # Figure out 2
    non_e_g = rev_known[1] | rev_known[4] | rev_known[7]
    e_g = rev_known[8].difference(non_e_g)
    rev_known[2] = [
        digit for digit in sample
        if len(digit) == 5 and e_g.issubset(digit)
        ][0]
    known[convert2string(rev_known[2])] = 2

    # Figure out 9
    rev_known[9] = [
        digit for digit in sample
        if len(digit) == 6 and not e_g.issubset(digit)
        ][0]
    known[rev_known[9]] = 9

    # Figure out 6
    # rev_known[1] == {c, f}
    rev_known[6] = [
        digit for digit in sample
        if len(digit) == 6 and not rev_known[1].issubset(digit)
        ][0]
    known[convert2string(rev_known[6])] = 6

    # Figure out 0
    rev_known[0] = [
        digit for digit in sample
        if len(digit) == 6 and digit not in known
        ][0]
    known[convert2string(rev_known[0])] = 0

    # Figure out 3
    rev_known[3] = [
        digit for digit in sample
        if len(digit) == 5 and rev_known[1].issubset(digit)
        ][0]
    known[convert2string(rev_known[3])] = 3

    # Figure out 5
    rev_known[5] = [digit for digit in sample if digit not in known][0]
    known[convert2string(rev_known[5])] = 5

    return (
        known[output[0]] * 1000 +
        known[output[1]] * 100 +
        known[output[2]] * 10 +
        known[output[3]]
        )


if __name__ == "__main__":
    test_input = [
        line.strip() for line in test_input.split("\n") if line.strip()
        ]
    real_input = parse_as_str("8-input.txt")
    assert(p1(test_input) == 26)
    print(p1(real_input))
    expected = [8394, 9781, 1197, 9361, 4873, 8418, 4548, 1625, 8717, 4315]
    try:
        for i, e in enumerate(expected):
            received = decode(test_input[i])
            assert(e == received)
    except AssertionError:
        print(f"Expected: {e}; received: {received}")
        raise
    try:
        received = p2(test_input)
        expected = 61229
    except AssertionError:
        print(f"Expected: {expected}; received: {received}")
        raise
    print(p2(real_input))
