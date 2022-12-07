import itertools

with open("3-input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    input_ = [[int(v.strip()) for v in line.split(" ") if v.strip()]
              for line in lines]


def part1():
    def calculate(data):
        total = 0
        permutations = {x: {0, 1, 2}.difference([x]) for x in range(3)}
        # {0: {1, 2}, 1: {0, 2}, 2: {0, 1}}
        for line in data:
            valid = True
            for h, oa in permutations.items():
                o, a = oa
                if line[h] >= (line[o] + line[a]):
                    valid = False
            if valid:
                total += 1
                print("Good: %s" % line)
            else:
                print("Bad: %s" % line)
        return total

    # test
    data = [
        # Bad
        [5, 10, 25],
        # Good
        [3, 4, 5],
        ]
    print("Expected 1, got %s" % calculate(data))
    print("Solution: %s" % calculate(input_))


def part2():

    def recombine_data(data):
        recombined = [list(zip(*data[i:i+3])) for i in range(0, len(data), 3)]
        return itertools.chain(*recombined)

    def calculate(data):
        # different algorithm as above calculate, but same output
        total = 0
        for line in data:
            line = list(line)  # In case it's coming in as tuple
            line.sort(reverse=True)
            if line[0] < sum(line[1:]):
                total += 1
        return total

    # Test
    test_input = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        ]
    print("Expected output 2x: [1 2 3] [4 5 6] [7 8 9]")
    print(list(recombine_data(test_input)))
    print("Solution: %s" % calculate(recombine_data(input_)))


part2()
