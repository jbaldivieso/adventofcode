"""For example:

Data from square 1 is carried 0 steps, since it's at the access port.
Data from square 12 is carried 3 steps, such as: down, left, left.
Data from square 23 is carried only 2 steps: up twice.
Data from square 1024 must be carried 31 steps.
How many steps are required to carry the data from the square identified in
your puzzle input all the way to the access port?

Your puzzle input is 325489.

"""

input_ = 325489

directions = {
    "right": {
        "move": lambda point: (point[0] + 1, point[1]),
        "left": lambda point: (point[0], point[1] + 1),
        "next": "up",
        },
    "up": {
        "move": lambda point: (point[0], point[1] + 1),
        "left": lambda point: (point[0] - 1, point[1]),
        "next": "left",
        },
    "left": {
        "move": lambda point: (point[0] - 1, point[1]),
        "left": lambda point: (point[0], point[1] - 1),
        "next": "down",
        },
    "down": {
        "move": lambda point: (point[0], point[1] - 1),
        "left": lambda point: (point[0] + 1, point[1]),
        "next": "right",
        }
    }


def part1():
    def calculate(target_square):
        coords = [(0, 0)]  # Start with 1st square (1) seeded; NB index is off!
        coords_as_set = set(coords)
        cur_dir = "right"
        for square in range(2, target_square + 1):
            next_point = directions[cur_dir]["move"](coords[-1])
            coords.append(next_point)
            coords_as_set.add(next_point)
            if directions[cur_dir]["left"](next_point) not in coords_as_set:
                cur_dir = directions[cur_dir]["next"]
        last = coords[-1]
        return abs(last[0]) + abs(last[1])

    print("1: 0")
    print(calculate(1))

    print("12: 3")
    print(calculate(12))

    print("23: 2")
    print(calculate(23))

    print("1024: 31")
    print(calculate(1024))

    print("Solution: %s" % calculate(input_))


def part2():

    def calculate(target):
        coords = [(0, 0)]  # Start with 1st square (1) seeded; NB index is off!
        values = {(0, 0): 1, }
        cur_dir = "right"

        def get_surrounding_squares_total(p):
            points = [
                (p[0]-1, p[1]+1), (p[0], p[1]+1), (p[0]+1, p[1]+1),
                (p[0]-1, p[1]  ),                 (p[0]+1, p[1]  ),
                (p[0]-1, p[1]-1), (p[0], p[1]-1), (p[0]+1, p[1]-1),
            ]
            return sum([values.get(pt, 0) for pt in points])

        latest_value = 1
        for value in range(2, target + 1):
            next_point = directions[cur_dir]["move"](coords[-1])
            coords.append(next_point)
            latest_value = get_surrounding_squares_total(next_point)
            values[next_point] = latest_value
            if latest_value > target:
                return latest_value
            if directions[cur_dir]["left"](next_point) not in values:
                cur_dir = directions[cur_dir]["next"]
        return latest_value

    print("Square 1: 1.")
    print(calculate(1))

    print("Square 2: 1.")
    print(calculate(2))

    print("Square 3: 2.")
    print(calculate(3))

    print("Square 4: 4.")
    print(calculate(4))

    print("Square 5: 5.")
    print(calculate(5))

    print("Solution: %s" % calculate(input_))


part2()
