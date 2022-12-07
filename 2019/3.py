from utils import parse_as_str


test_input = [
    (["R8", "U5", "L5", "D3"],
     ["U7", "R6", "D4", "L4"],
     6, 30),
    (["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"],
     ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"],
     159, 610),
    (["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"],
     ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"],
     135, 410)
    ]


class Segment(object):

    def __init__(self, start, end):
        """Both args are coordinates (tuples)"""
        self.start = start
        self.end = end

    def __repr__(self):
        return f"Segment from {self.start} to {self.end}"

    @property
    def sorted_xs(self):
        return sorted([self.start[0], self.end[0]])

    @property
    def sorted_ys(self):
        return sorted([self.start[1], self.end[1]])

    @property
    def distance(self):
        return (
            abs(self.sorted_xs[1] - self.sorted_xs[0]) +
            abs(self.sorted_ys[1] - self.sorted_ys[0])
            )

    def get_intersection(self, other):
        """Return coordinates (tuple) of where @other intersects w/ self, else
        None.
        """
        # Parallel lines: vertical
        if self.start[0] == self.end[0] and other.start[0] == other.end[0]:
            return
        # Parallel lines: horizontal
        if self.start[1] == self.end[1] and other.start[1] == other.end[1]:
            return
        # self is vertical
        if self.start[0] == self.end[0]:
            low, high = other.sorted_xs
            if low <= self.sorted_xs[0] <= high:
                # The above meant that other crosses self from horizontally.
                # What about vertically?
                low, high = self.sorted_ys
                if low <= other.sorted_ys[1] <= high:
                    # So they do intersect!
                    return (self.start[0], other.start[1])
        else:
            # self is horizontal
            low, high = other.sorted_ys
            if low <= self.sorted_ys[1] <= high:
                low, high = self.sorted_xs
                if low <= other.sorted_xs[0] <= high:
                    # So they do intersect!
                    return (other.start[0], self.start[1])


def parse_point(p):
    return (p[0], int(p[1:]))


def get_distance_from_origin(pt):
    return abs(pt[0]) + abs(pt[1])


def parse_file(name):
    """Returns list of lists of, e.g., "R55"."""
    lines = parse_as_str(name)
    return [[parse_point(i) for i in line.split(",")] for line in lines]


def get_segments(wire):
    """@wire is a list of instruction tuples (dir (char), dist). Return a list
    of Segments.
    """
    last = (0, 0)
    results = []
    for direction, distance in wire:
        if direction == "U":
            pt = (last[0], last[1] + distance)
        elif direction == "D":
            pt = (last[0], last[1] - distance)
        elif direction == "L":
            pt = (last[0] - distance, last[1])
        elif direction == "R":
            pt = (last[0] + distance, last[1])
        results.append(Segment(last, pt))
        last = pt
    return results


def get_intersection(s1, s2):
    """Both args are lists of Segments"""
    intersections = [seg1.get_intersection(seg2) for seg1 in s1 for seg2 in s2]
    intersections = [i for i in intersections if i and i != (0, 0)]
    return min(intersections, key=get_distance_from_origin)


def get_intersection_distances(w1, w2):
    """Return a list of all of the total distances traveled by both @w1 and @w2
    to get to all of the (non-origin) intersections btw the two wires.

    ("Wires" @w1 & @w2 are just lists of Segments.)
    """
    results = []
    d1 = 0  # Cumulative distance
    for seg1 in w1:
        d2 = 0
        for seg2 in w2:
            i = seg1.get_intersection(seg2)
            if i and i != (0, 0):
                seg1_partial = Segment(seg1.start, i)
                seg2_partial = Segment(seg2.start, i)
                results.append(
                    d1 + d2 + seg2_partial.distance + seg1_partial.distance
                    )
            # We add on the total segment distance afterwards, bc the last bit
            # traveled to the intersection is probably less than the last
            # segments' entire length.
            d2 += seg2.distance
        d1 += seg1.distance
    return results


def part1(w1, w2):
    s1 = get_segments(w1)
    s2 = get_segments(w2)
    intersection = get_intersection(s1, s2)
    return get_distance_from_origin(intersection)


def part2(w1, w2):
    w1 = get_segments(w1)
    w2 = get_segments(w2)
    distances = get_intersection_distances(w1, w2)
    return min(distances)


# Test our intersection logic first
a = Segment((2, 1), (2, 3))
b = Segment((1, 2), (3, 2))
c = Segment((1, 4), (3, 4))

assert a.get_intersection(b) == (2, 2)
assert a.get_intersection(c) is None
assert b.get_intersection(a) == (2, 2)

for w1, w2, expected, _ in test_input:
    w1 = [parse_point(i) for i in w1]
    w2 = [parse_point(i) for i in w2]
    assert part1(w1, w2) == expected


wire1, wire2 = parse_file('3-input.txt')
print(f"Part 1 result: {part1(wire1, wire2)}")


for w1, w2, _, expected in test_input:
    w1 = [parse_point(i) for i in w1]
    w2 = [parse_point(i) for i in w2]
    print(f"Got {part2(w1, w2)}; expected {expected}")
    assert part2(w1, w2) == expected

print(f"Part 2 result: {part2(wire1, wire2)}")
