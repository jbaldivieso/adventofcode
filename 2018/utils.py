from pathlib import Path


def parse_as_str(name):
    path = Path(name)
    with open(path, "r") as f:
        results = f.readlines()
    results = [l.strip() for l in results]
    return results


def parse_as_ints(name):
    return [int(l) for l in parse_as_str(name)]


parseAsStr = parse_as_str
parseAsInts = parse_as_ints
