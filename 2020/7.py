import re


test_input = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

test_input2 = """
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""

parsing_test = [
    ("light red bags contain 1 bright white bag, 2 muted yellow bags.",
     ("light red", {
         "bright white": 1,
         "muted yellow": 2,
         })
     ),
    ("dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
     ("dark orange", {
         "bright white": 3,
         "muted yellow": 4,
         })
     ),
    ("faded blue bags contain no other bags.",
     ("faded blue", {}),
     ),
    ]

pattern = re.compile(r"(?P<number>\d+) (?P<color>[\w ]+) bags?")


def parse_line(line):
    """Return a tuple like (color, dependencies) where dependencies is a dict
    like {
            color: "color",
            number: x,
        }
    """
    color, _, remainder = line.partition(" bags contain ")
    if remainder.startswith("no"):
        return (color, {})
    if remainder.endswith("."):
        remainder = remainder[:-1]
    dependencies = {}
    for part in remainder.split(", "):
        try:
            match = re.match(pattern, part).groupdict()
        except AttributeError:
            print(f"No match for '{part}' (line: {line})")
            raise
        number = int(match["number"])
        dependencies[match["color"]] = number
    return (color, dependencies)


def parse_data(data):
    regulations = Regulations()
    for line in data.split("\n"):
        if not line:
            continue
        color, dependencies = parse_line(line)
        regulations[color] = dependencies
    return regulations


class Regulations(dict):

    def can_contain(self, desired, current_color):
        if desired in self[current_color]:
            return True
        if self[current_color]:
            return any(
                self.can_contain(desired, color)
                for color in self[current_color]
                )
        return False

    def get_bag_count(self, desired):
        immediate_contents = sum(self[desired].values())
        dependencies_contents = sum([
            count * self.get_bag_count(color)
            for color, count in self[desired].items()
            ])
        return immediate_contents + dependencies_contents


def p1(data, desired_color):
    regulations = parse_data(data)
    count = 0
    for color in regulations:
        if color == desired_color:
            continue
        if regulations.can_contain(desired_color, color):
            count += 1
    return count


def p2(data, desired_color):
    regulations = parse_data(data)
    return regulations.get_bag_count(desired_color)


if __name__ == "__main__":
    with open("7-input.txt") as f:
        data = f.read()
    for line, expected in parsing_test:
        assert(parse_line(line) == expected)
    print(p1(data, "shiny gold"))
    assert(p2(test_input, "shiny gold") == 32)
    assert(p2(test_input2, "shiny gold") == 126)
    print(p2(data, "shiny gold"))
