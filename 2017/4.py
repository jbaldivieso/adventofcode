from collections import Counter

with open("4-input.txt", "r") as f:
    input_ = [line.strip() for line in f.readlines()]

print(input_[0])


def part1():
    def is_valid(l):
        c = Counter(l.split(" "))
        val, count = c.most_common(1)[0]
        return count == 1

    print('"aa bb cc dd ee" is valid.')
    print(is_valid("aa bb cc dd ee"))

    print('"aa bb cc dd aa" is not valid')
    print(is_valid("aa bb cc dd aa"))

    print('"aa bb cc dd aaa" is valid')
    print(is_valid("aa bb cc dd aaa"))

    print("Solution: ", end="")
    print(sum([1 for line in input_ if is_valid(line)]))


def part2():
    def is_valid(l):
        c = Counter([tuple(sorted(w)) for w in l.split(" ")])
        val, count = c.most_common(1)[0]
        return count == 1

    print('"abcde fghij" is a valid passphrase.')
    print(is_valid("abcde fghij"))

    print('"abcde xyz ecdab" is not valid')
    print(is_valid("abcde xyz ecdab"))

    print('"a ab abc abd abf abj" is valid')
    print(is_valid("a ab abc abd abf abj"))

    print('"iiii oiii ooii oooi oooo" is valid.')
    print(is_valid("iiii oiii ooii oooi oooo"))

    print('"oiii ioii iioi iiio" is not valid')
    print(is_valid("oiii ioii iioi iiio"))

    print("Solution: ", end="")
    print(sum([1 for line in input_ if is_valid(line)]))


part2()
