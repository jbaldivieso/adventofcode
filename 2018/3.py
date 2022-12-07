import re

from utils import parseAsStr


pattern = re.compile(
    r"#(?P<id>\d+) @ (?P<left_offset>\d+),(?P<top_offset>\d+): "
    r"(?P<width>\d+)x(?P<height>\d+)")


def parse_input(line):
    """Returns a dict like {
        'id': 1,
        'left_offset': 1, 'top_offset': 3,
        'width': 4, 'height': 4,
        }
    """
    return {k: int(v) for k, v in re.match(pattern, line).groupdict().items()}


def get_coordinates_from_claim(claim):
    """Returns a list of (x, y) tuples."""
    squares = []
    for x in range(claim["width"]):
        for y in range(claim["height"]):
            squares.append((x + claim["left_offset"], y + claim["top_offset"]))
    return squares


data = parseAsStr("3-input.txt")
data = [parse_input(claim) for claim in data]


def part1(data):
    squares_covered = set()
    overlaps = set()
    for claim in data:
        squares = get_coordinates_from_claim(claim)
        for square in squares:
            if square in squares_covered:
                overlaps.add(square)
            else:
                squares_covered.add(square)
    return len(overlaps)


test_data = [
    "#1 @ 1,3: 4x4",
    "#2 @ 3,1: 4x4",
    "#3 @ 5,5: 2x2",
    ]
test_data = [parse_input(claim) for claim in test_data]


assert part1(test_data) == 4

print("Made it through part 1 tests")
print(f"Part 1: {part1(data)}")


def part2(data):
    overlapped_coordinates = set()
    clean_candidates = {}
    for claim in data:
        # Convert this claim to a set of (x, y) tuples
        this_square = set(get_coordinates_from_claim(claim))
        # Compare this_square to each candidate: if it overlaps, both squares
        # go into the set of overlapped coordinates, and the clean candidate is
        # weeded out of the candidate pool.
        poppers = []
        for id, square in clean_candidates.items():
            if this_square.intersection(square):
                overlapped_coordinates.update(this_square)
                overlapped_coordinates.update(square)
                poppers.append(id)
        for popper in poppers:
            clean_candidates.pop(popper)
        # Regardless of how the above played out, check to see whether our
        # current square belongs in the overlaps or the clean candidates.
        if this_square.intersection(overlapped_coordinates):
            overlapped_coordinates.update(this_square)
        else:
            clean_candidates[claim["id"]] = this_square
    if len(clean_candidates) == 1:
        return list(clean_candidates.keys())[0]
    else:
        return f"Failed: had {len(clean_candidates)} clean candidates"


assert part2(test_data) == 3

print("Made it through part 2 tests")
print(f"Part 1: {part2(data)}")
