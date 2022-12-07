directions = (
    "R2, L1, R2, R1, R1, L3, R3, L5, L5, L2, L1, R4, R1, R3, L5, L5, R3, L4, "
    "L4, R5, R4, R3, L1, L2, R5, R4, L2, R1, R4, R4, L2, L1, L1, R190, R3, "
    "L4, R52, R5, R3, L5, R3, R2, R1, L5, L5, L4, R2, L3, R3, L1, L3, R5, L3, "
    "L4, R3, R77, R3, L2, R189, R4, R2, L2, R2, L1, R5, R4, R4, R2, L2, L2, "
    "L5, L1, R1, R2, L3, L4, L5, R1, L1, L2, L2, R2, L3, R3, L4, L1, L5, L4, "
    "L4, R3, R5, L2, R4, R5, R3, L2, L2, L4, L2, R2, L5, L4, R3, R1, L2, R2, "
    "R4, L1, L4, L4, L2, R2, L4, L1, L1, R4, L1, L3, L2, L2, L5, R5, R2, R5, "
    "L1, L5, R2, R4, R4, L2, R5, L5, R5, R5, L4, R2, R1, R1, R3, L3, L3, L4, "
    "L3, L2, L2, L2, R2, L1, L3, R2, R5, R5, L4, R3, L3, L4, R2, L5, R5"
    )


def change_direction(cur_dir, turn):
    """return new val for cur_dir"""
    left = {
        "N": "W",
        "W": "S",
        "S": "E",
        "E": "N"
        }
    right = {v: k for k, v in left.items()}
    map_ = left if turn == "L" else right
    return map_[cur_dir]


def walk(steps, cur_dir, coords):
    """Return new val for coords"""
    x, y = coords
    if cur_dir == "N":
        y += steps
    elif cur_dir == "E":
        x += steps
    elif cur_dir == "S":
        y -= steps
    elif cur_dir == "W":
        x -= steps
    return (x, y)


def half1():
    directions = [d.strip() for d in directions.split(",")]
    coords = (0, 0)
    cur_dir = "N"

    for move in directions:
        turn = move[0]
        steps = int(move[1:])
        cur_dir = change_direction(cur_dir, turn)
        coords = walk(steps, cur_dir, coords)

    print(coords)
    print(sum([abs(v) for v in coords]))


class Segment(object):
    orientation = None  # h or v
    range_ = (0, 0)  # value to value
    intercept = None  # if orientation is horizontal, this is y val, else x

    def __init__(self, **kw):
        for key, value in kw.items():
            setattr(self, key, value)

    def get_intersection(self, other_segment):
        """Returns tuple of coordinates where self and other_segment
        intersect, if they do, otherwise None.

        Assume that if they share the same orientation, they don't
        intersect.
        """
        if self.orientation == other_segment.orientation:
            return None
        result = [None, None]

        def test(val, lower, upper):
            return lower <= val <= upper

        if test(self.intercept, *other_segment.range_):
            if self.orientation == "h":
                result[1] = self.intercept
            else:
                result[0] = self.intercept
            if test(other_segment.intercept, *self.range_):
                if other_segment.orientation == "h":
                    result[1] = other_segment.intercept
                else:
                    result[0] = other_segment.intercept
                return result
        return None


def half2():
    def calculate(data):
        segments = []
        data = [d.strip() for d in data.split(",")]
        coords = (0, 0)
        cur_dir = "N"
        for move in data:
            turn = move[0]
            steps = int(move[1:])
            new_dir = change_direction(cur_dir, turn)
            new_coords = walk(steps, new_dir, coords)
            orientation = "h" if new_dir in ("W", "E") else "v"
            if orientation == "h":
                range_ = (new_coords[0], coords[0])
            else:
                range_ = (new_coords[1], coords[1])
            if range_[0] > range_[1]:
                range_ = (range_[1], range_[0])
            segment = Segment(
                orientation=orientation,
                range_=range_,
                intercept=coords[1] if orientation == "h" else coords[0],
                )
            # Skip the most recent point, since by definition, it left off where
            # this one picked up!
            for other in segments[:-1]:
                intersection = segment.get_intersection(other)
                if intersection:
                    print("Found it! %s" % intersection)
                    return sum([abs(v) for v in intersection])
            segments.append(segment)
            cur_dir = new_dir
            coords = new_coords

    # Test
    # For example, if your instructions are R8, R4, R4, R8, the first location
    # you visit twice is 4 blocks away, due East.
    print("R8, R4, R4, R8 should be 4 blocks")
    print(calculate("R8, R4, R4, R8"))

    print("And the solution:")
    print(calculate(directions))


half2()
