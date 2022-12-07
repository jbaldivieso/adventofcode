from collections import defaultdict

from utils import parse_as_str

test_input = [
    (1, 1),
    (1, 6),
    (8, 3),
    (3, 4),
    (5, 5),
    (8, 9),
    ]

data = parse_as_str("6-input.txt")
data = [tuple([int(n) for n in s.split(", ")]) for s in data]


# Subclass set so we can handily paste a flag on it
class MySet(set):
    touches_edge = False


def get_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_bounding_box(data):
    """Return a list of two x/y tuples marking the top left and bottom right
    points of the bounding box.
    """
    xs, ys = zip(*data)
    return [(min(xs), min(ys)), (max(xs), max(ys))]


def part1(data):

    def determine_owner(pt):
        """Returns the (x, y) tuple of the coordinate (from data) that is the
        closest to pt.
        """
        # List of tuples: (coordinate, distance to pt)
        distances = [(coord, get_distance(coord, pt)) for coord in data]
        distances.sort(key=lambda t: t[1])
        if distances[0][1] != distances[1][1]:
            return distances[0][0]
        else:
            return None

    # Determine bounding box
    box = get_bounding_box(data)

    # Assign each point in the bounding box to one of the coordinates
    territories = defaultdict(MySet)
    for x in range(box[0][0], box[1][0] + 1):
        for y in range(box[0][1], box[1][1] + 1):
            pt = (x, y)
            owner = determine_owner(pt)
            if owner:
                territories[owner].add(pt)
                is_edge = (
                    x in (box[0][0], box[1][0]) or
                    y in (box[0][1], box[1][1])
                    )
                if is_edge:
                    territories[owner].touches_edge = True

    # Throw out the points whose boxes touch the borders of our bounding box
    sizes = [len(v) for v in territories.values() if not v.touches_edge]
    return max(sizes)


assert part1(test_input) == 17
print("Finished with part 1 tests")
print(f"Part 1 results: {part1(data)}")


def part2(data, limit):
    box = get_bounding_box(data)
    territory = []
    for x in range(box[0][0], box[1][0] + 1):
        for y in range(box[0][1], box[1][1] + 1):
            distance = 0
            for pt in data:
                distance += get_distance(pt, (x, y))
                if distance >= limit:
                    break
            if distance < limit:
                territory.append((x, y))
    return len(territory)


assert part2(test_input, 32) == 16
print("Done with part2 tests")
print(f"Part 2 results: {part2(data, 10000)}")
