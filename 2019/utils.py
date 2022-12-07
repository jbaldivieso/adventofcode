from pathlib import Path


def parse_as_str(name):
    path = Path(name)
    with open(path, "r") as f:
        results = f.readlines()
    results = [l.strip() for l in results]
    return results


def parse_as_ints(name, delimiter=None):
    lines = parse_as_str(name)
    if delimiter:
        # Assume a single line
        lines = [l.strip() for l in lines[0].split(delimiter)]
    return [int(l) for l in lines]


parseAsStr = parse_as_str
parseAsInts = parse_as_ints
