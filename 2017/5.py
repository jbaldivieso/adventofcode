with open("5-input.txt", "r") as f:
    input_ = [int(line.strip()) for line in f.readlines()]


def part1():
    def calculate(series):
        index = steps = 0
        while True:
            try:
                current = series[index]
            except IndexError:
                return steps
            series[index] += 1
            steps += 1
            index += current

    print("with input 0, 3, 0, 1, -3 expect 5")
    print(calculate([0, 3, 0, 1, -3]))

    print(calculate(input_))


def part2():
    def calculate(series):
        index = steps = 0
        while True:
            try:
                current = series[index]
            except IndexError:
                return steps
            if current >= 3:
                series[index] -= 1
            else:
                series[index] += 1
            steps += 1
            index += current

    print("with input 0, 3, 0, 1, -3 expect 10")
    print(calculate([0, 3, 0, 1, -3]))

    print(calculate(input_))


part2()
