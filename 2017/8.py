from collections import defaultdict
import re


with open("8-input.txt", "r") as f:
    raw_input_ = [line.strip() for line in f.readlines()]

test_input = [
    "b inc 5 if a > 1",
    "a inc 1 if b < 5",
    "c dec -10 if a >= 1",
    "c inc -20 if c == 10",
    ]

operations = {
    "inc": lambda var, val: var + val,
    "dec": lambda var, val: var - val,
    }

compiled = re.compile(
    r"(?P<var1>\w+) (?P<operation>inc|dec) (?P<amt>.*) if (?P<var2>\S*) "
    r"(?P<clause>.*)")


def parse_line(line):
    """take a string and return dict with:
    * register name ('var1')
    * operation (ref to function)
    * expression as string, with if/else statement (else part added) ('clause')
    """
    results = compiled.match(line).groupdict()
    results["clause"] = (
        "%(amt)s if registers['%(var2)s'] %(clause)s else 0" % results
        )
    return results


def part1():
    def process(input_):
        registers = defaultdict(int)
        for line in input_:
            data = parse_line(line)
            registers[data["var1"]] = operations[data["operation"]](
                registers[data["var1"]], eval(data["clause"])
                )
        return max(registers.values())

    print("Expect 1, got %s" % process(test_input))
    print("Solution: %s" % process(raw_input_))


def part2():
    def process(input_):
        max_ = 0
        registers = defaultdict(int)
        for line in input_:
            data = parse_line(line)
            registers[data["var1"]] = operations[data["operation"]](
                registers[data["var1"]], eval(data["clause"])
                )
            max_ = max((max_, max(registers.values())))
        return max_

    print("Expect 10, got %s" % process(test_input))
    print("Solution: %s" % process(raw_input_))


part2()
