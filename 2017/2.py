import csv


with open("2-input.csv", "r") as f:
    input_ = csv.reader(f.readlines(), delimiter='\t')
    input_ = [[int(s) for s in line] for line in input_]



def part1():
    def calculate(data):
        total = 0
        for line in data:
            total += max(line) - min(line)
        return total
    test_data = [
        [5, 1, 9, 5, ],
        [7, 5, 3, ],
        [2, 4, 6, 8, ],
        ]
    print("With test data, expecting result: 18")
    print(calculate(test_data))

    print("Solution: %s" % calculate(input_))


def part2():

    def calculate(data):

        def process_value(val, line):
            # Assumes val is unique in line
            result = 0
            for other in line:
                if val > other:
                    if val % other == 0:
                        result += val / other
            return result

        total = 0
        for line in data:
            total += sum([process_value(i, line) for i in line
                          if process_value(i, line)])
        return total

    test_data = [
        [5, 9, 2, 8],
        [9, 4, 7, 3],
        [3, 8, 6, 5],
        ]
    print("With test data, expecting result: 9")
    print(calculate(test_data))

    print("Solution: %s" % calculate(input_))

# part1()
part2()
