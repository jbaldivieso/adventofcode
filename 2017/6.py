input_ = [10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6]


def part1():
    def calculate(data):
        prev = {tuple(data)}
        count = 0
        while True:
            count += 1
            to_allocate = max(data)
            index = data.index(to_allocate)
            data[index] = 0
            while True:
                index += 1
                try:
                    data[index] += 1
                except IndexError:
                    index = 0
                    data[index] += 1
                to_allocate -= 1
                if not to_allocate:
                    break
            if tuple(data) in prev:
                return count
            else:
                prev.add(tuple(data))

    test_input = [0, 2, 7, 0]
    print("Test: expecting 5; got %s" % calculate(test_input))
    print("Solution: %s" % calculate(input_))


def part2():
    def calculate(data, get_count=False):
        prev = {tuple(data)}
        count = 0
        while True:
            count += 1
            to_allocate = max(data)
            index = data.index(to_allocate)
            data[index] = 0
            while True:
                index += 1
                try:
                    data[index] += 1
                except IndexError:
                    index = 0
                    data[index] += 1
                to_allocate -= 1
                if not to_allocate:
                    break
            if tuple(data) in prev:
                return count if get_count else data
            else:
                prev.add(tuple(data))

    test_input = [0, 2, 7, 0]
    repeat_series = calculate(test_input)
    print("Test: expecting 4; got %s" % calculate(repeat_series, get_count=True))
    repeat_series = calculate(input_)
    print("Solution: %s" % calculate(repeat_series, get_count=True))


part2()
